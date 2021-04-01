#!/usr/bin/env python
# coding: utf-8

# 
# # Numba: Compilation "Just in Time" (jit)
# 
# Numba converts Python functions into optimized machine code at runtime using the standard LLVM compiler library. Then the numerical algorithms compiled by Numba in Python can approach the speeds of C or FORTRAN, where the classic loops like in R and matlab, can be a bit slow.
# 
# https://numba.pydata.org/ see also https://numba.pydata.org/numba-doc/dev/user/jit.html

# %%


import numpy as np
import matplotlib.pyplot as plt
import time
from numba import jit, njit, prange
import matplotlib.animation as animation
get_ipython().run_line_magic('matplotlib', 'inline')
from IPython.display import HTML


# # Example 1: Monte Carlo method to approach $\pi$
# See https://numba.pydata.org/numba-doc/dev/glossary.html#term-nopython-mode for why typing `nopython=True` below.
# 
# The underlying idea of this function is to approximate $\pi$ using a simple procedure:
# generate points uniformly at random in the set $[0,1] \times [0,1]$. Keep only the points whose Euclidean norm is smaller than 1. The ratio of points in this area w.r.t. the total number of points is the ratio between the area of this region and the one of $[0,1] \times [0,1]$. It is easy to check that this ratio is $\pi/4$

# %%


fig = plt.figure(figsize=(8,8))
circle1 = plt.Circle((0, 0), 1, color='orange')
ax = fig.gca()
ax.add_artist(circle1)
ax.set_aspect('equal')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
targeted = 0

n_samples = 101
lst = np.zeros(n_samples)
coordinates = []
for sample in range(1, n_samples):
    vec = np.random.rand(2)
    if np.linalg.norm(vec) < 1.:
        plt.plot(vec[0], vec[1], 'ok')
        targeted += 1
        lst[sample] = 1
    else:
        plt.plot(vec[0], vec[1], 'xr', markersize=5)
    coordinates.append(vec)
    ax.set_title('4 x Ratio of points over all draws: 4 x {0}/{1}={2}'.format(targeted, sample, 4  *targeted/sample))
plt.show()


# %%



targeted = 0
n_samples = 200
lst = np.zeros(n_samples)
vec = np.random.rand(2, n_samples)
current_ratio = np.zeros(n_samples)
for sample in range(n_samples):
    if np.linalg.norm(vec[:, sample]) < 1.:
        targeted += 1
        lst[sample] = 1
    current_ratio[sample] = targeted / (sample+1)

xdata_in, ydata_in = [], []
xdata_out, ydata_out = [], []
xconv, yconv = [], []
xpoint, ypoint = [], []

fig, (ax, ax2) = plt.subplots(1, 2, figsize=(13, 6))

ln_in, = ax.plot([], [], 'ok', label='in')
ln_out, = ax.plot([], [], 'xr', markersize=8, label='out')
line_conv, = ax2.plot([], [], '-', color='k',
                      label='Monte Carlo Estimate')
point_conv, = ax2.plot([], [], 'o', color='k')

ax2.plot(np.arange(n_samples), np.full(
    (n_samples,), np.pi/4), '--k', label=r'True Area (Orange part): $\frac{\pi}{4}$')


def init():
    circle1 = plt.Circle((0, 0), 1, color='orange')
    ax.add_artist(circle1)
    ax.set_aspect('equal')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.legend(bbox_to_anchor=(-0.04, 0.75))

    ax2.set_xlim([1, n_samples + 1])
    ax2.set_ylim([0, 1])
    ax2.legend(loc=4)

    return ln_in, ln_out, line_conv, point_conv


def update(frame):
    if lst[frame] > 0.5:
        xdata_in.append(vec[0, frame])
        ydata_in.append(vec[1, frame])
        ln_in.set_data(xdata_in, ydata_in)
    else:
        xdata_out.append(vec[0, frame])
        ydata_out.append(vec[1, frame])
        ln_out.set_data(xdata_out, ydata_out)
    ax.set_title('Ratio of points over all draws: {0:0.2}'.format(
        current_ratio[frame]))
    ax2.set_title('Monte Carlo: convergence trough iterates')

    xconv.append(frame+1)
    yconv.append(current_ratio[frame])

    line_conv.set_data(xconv, yconv)
    point_conv.set_data(frame+1, current_ratio[frame])
    return ln_in, ln_out, line_conv, point_conv


ani = animation.FuncAnimation(fig, update, frames=n_samples, interval=150,
                              init_func=init, blit=True)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save('pi.mp4', writer=writer)
plt.show()


# %%

from IPython.display import Video
Video("pi.mp4")  # Need ffmpeg installed on your machine


# %%


# Reminder: orange area is:
np.pi/4


# %%


@jit(nopython=True)
def monte_carlo_pi(n_samples=1000):
    acc = 0
    for sample in range(n_samples):
        vec = np.random.rand(2)
        if np.linalg.norm(vec) < 1.:
            acc += 1
    return 4.0 * acc / n_samples

@jit(nopython=True)
def monte_carlo_pi_bis(n_samples=1000):
    acc = 0
    for sample in range(n_samples):
        vec = np.random.rand(2)
        if np.linalg.norm(vec) < 1.:
            acc += 1
    return acc


n_samples = 1000000
pi_approx = monte_carlo_pi_bis(n_samples=n_samples)
# %%
# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!
start = time.time()
n_samples = 1000000
pi_approx = monte_carlo_pi(n_samples=n_samples)
end = time.time()
print("Elapsed (with compilation) = %s" % (end - start))

# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
start = time.time()
pi_approx = monte_carlo_pi(n_samples=n_samples)
end = time.time()
print("Elapsed (after compilation) = %s" % (end - start))


# # Example 2: matrix function (without using numpy)

# %%

def go_slow(A):  # Function is compiled and runs in machine code
    trace = 0
    for i in range(A.shape[0]):
        trace += A[i, i]
    return trace


all_n_samples = [1000, 5000, 10000]
t0 = []
t1 = []
t2 = []

for n_samples in all_n_samples:
    print(n_samples)
    x = np.arange(n_samples ** 2).reshape(n_samples, n_samples)

    @jit(nopython=True)
    def go_fast(a):  # Function is compiled and runs in machine code
        trace = 0
        for i in range(a.shape[0]):
            trace += a[i, i]
        return trace
    # COMPILATION IS INCLUDED!
    start = time.time()
    go_fast(x)
    end = time.time()
    t0.append(end - start)
    print("Elapsed (with compilation) = %s" % (end - start))
    # COMPILATION IS NOT INCLUDED, RUN FROM CACHE
    start = time.time()
    go_fast(x)
    end = time.time()
    t1.append(end - start)
    print("Elapsed (after compilation) = %s" % (end - start))
    # VANILLA PYTHON
    start = time.time()
    go_slow(x)
    end = time.time()
    t2.append(end - start)
    print("Elapsed (vanilla) = %s" % (end - start))


t0 = np.array(t0)
t1 = np.array(t1)
t2 = np.array(t2)


print(all_n_samples)
print("Percentage improvements over vanilla code")
print((t0 - t2) / t2 * 100)
print((t1 - t2) / t2 * 100)


# # Example 3: Gradient descent with / without numba

# %%

n_samples = 1000
n_features = 500
n_iterations = 2000

# OLS: of y and X

X = np.random.randn(n_samples, n_features)
y = np.random.randn(n_samples)
y[n_samples // 2:] = 0


# init = 0
w = np.zeros(n_features)


# %%

# Function objective for OLS:
# min \|y - X w \|^2 / 2 := f(w)

# f(w) =  < y - Xw ; y - Xw>/2 = (y - Xw)^\top (y - Xw)/2
# f(w) = w^\top X^\top Xw / 2  - (X^\top y)^\top w
# \nabla f(w) = X^\top X w - X^\top y
# in Python : (X.T.dot(X.dot(w) - y)

@jit(nopython=True)
# Function is compiled and runs in machine code
def gradient(X, y, w, step_size=0.01,  max_iter=1000):
    """Gradient descent with constant step size."""
    for k in range(max_iter):
        w -=  step_size * (X.T.dot(X.dot(w) - y))
    return w

# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!
start = time.time()
gradient(X, y, w)
end = time.time()
print("Elapsed (with compilation) = %s" % (end - start))

# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
start = time.time()
gradient(X, y, w)
end = time.time()
print("Elapsed (after compilation) = %s" % (end - start))




# ### For  more on numba:
# 



# Parallelization: https://numba.pydata.org/numba-doc/dev/user/parallel.html

# In addition to being able to compile your code in low-level language,
# Numba allows you to parallelize your loops, which can be useful in case you do Monte Carlo.

# We simply take the previous code allowing to compute an estimate of pie,
# to which we add the option parralel = True on one hand and we replace range
# by prange on the other hand.

# %%
@njit(parallel=True)
def monte_carlo_pi_parrallel(n_samples=1000):
    acc = 0
    for sample in prange(n_samples):
        vec = np.random.rand(2)
        if np.linalg.norm(vec) < 1.:
            acc += 1
    return 4.0 * acc / n_samples 

# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!

# compilation
monte_carlo_pi_parrallel(n_samples=10**2)

# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
start = time.time()
monte_carlo_pi(n_samples=10**7)
end = time.time()
print("Elapsed without parallelization = %s" % (end - start))

start = time.time()
monte_carlo_pi_parrallel(n_samples=10**7)
end = time.time()
print("Elapsed with parallelization = %s" % (end - start))


# For Numba to compile your code in low-level language, you must use functions
# that the package takes into account. For example, many functions of Numpy are
# supported:
#  https://numba.pydata.org/numba-doc/dev/reference/numpysupported.html




# %%
# # Example 4: Logistic regression

# %%
# n_samples = 100
# n_features = 20
y = np.random.randint(2, size=n_samples)*2 - 1
print(y)
w = np.zeros(n_features)  # init = 0


# %%

def logistic_regression_no_jit(y, X, w, iterations=1000):
    for i in range(iterations):
        w -= np.dot(((1.0 / (1.0 + np.exp(-y * np.dot(X, w))) - 1.0) * y), X)
    return w


# %%


start = time.time()
w = logistic_regression_no_jit(y, X, w, iterations=n_iterations )
end = time.time()
print("Elapsed (with compilation) = %s" % (end - start))


# %%

@jit(nopython=True)
def logistic_regression(y, X, w, iterations=1000):
    for i in range(iterations):
        w -= np.dot(((1.0 / (1.0 + np.exp(-y * np.dot(X, w))) - 1.0) * y), X)
    return w


# %%


# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!
start = time.time()
logistic_regression(y, X, w, iterations=n_iterations)
end = time.time()
print("Elapsed (with compilation) = %s" % (end - start))

# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
start = time.time()
logistic_regression(y, X, w, iterations=n_iterations)
end = time.time()
print("Elapsed (after compilation) = %s" % (end - start))


# %%


# Write a function using Numba to test if an element 'i' belongs to an array.
# The result should be similar to the following example:
i = 10
array = np.arange(11)
i in array

# Prediction of a logistic model:

# First, you will write a function to generate a classification dataset
# dependent on a single predictor variable without intercept. Thus, the
# function takes as input x and its coefficients and will return a variable
# to predict y. To generate the noise, we can use a function that predicts 0
# or 1 to add to the signal. The coefficients equal to 2 will be modified
# to be 1.

# You will take care to measure computing time for each of these functions!

# Then, you will write a function (using Numba) allowing to predict a logistic
# model already learned (we will use sklearn for the learning, the previous
# function not working for scalars). We will check that our function finds the
# same results as the predict_proba function of sklearn.

# We will finish by making a graph to show the evolution of the prediction
# curve as a function of the value of x.



@njit(parallel=False)
def do_sum_parallel(A):
    # each thread can accumulate its own partial sum, and then a cross
    # thread reduction is performed to obtain the result to return
    n = len(A)
    acc = 0.
    for i in prange(n):
        acc += np.sqrt(A[i])
    return acc

@njit(parallel=True, fastmath=True)
def do_sum_parallel_fast(A):
    n = len(A)
    acc = 0.
    for i in prange(n):
        acc += np.sqrt(A[i])
    return acc

A = np.random.randn(10000)
# %%

%%time
do_sum_parallel(A)
# %%
%%time
do_sum_parallel_fast(A)
# %%
