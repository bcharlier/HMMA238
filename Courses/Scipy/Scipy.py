#!/usr/bin/env python
# coding: utf-8

# # SciPy - Librairie d'algorithmes pour le calcul scientifique en Python
#
#       Joseph Salmon : joseph.salmon@umontpellier.fr
#
# Adapted from
#
# - A. Gramfort (alexandre.gramfort@inria.fr) http://alexandre.gramfort.net/
# - J.R. Johansson (robert@riken.jp) http://dml.riken.jp/~rob/

# ## Introduction
#
# SciPy build upon NumPy.
#
#
# Among others, SciPy deals with:
#
# * Integration ([scipy.integrate](http://docs.scipy.org/doc/scipy/reference/integrate.html))
# * Optimization ([scipy.optimize](http://docs.scipy.org/doc/scipy/reference/optimize.html))
# * Interpolation ([scipy.interpolate](http://docs.scipy.org/doc/scipy/reference/interpolate.html))
# * Fourier Transform ([scipy.fftpack](http://docs.scipy.org/doc/scipy/reference/fftpack.html))
# * Signal Processing ([scipy.signal](http://docs.scipy.org/doc/scipy/reference/signal.html))
# * Linear Algebra ([scipy.linalg](http://docs.scipy.org/doc/scipy/reference/linalg.html))
# * *Sparse* matrices ([scipy.sparse](http://docs.scipy.org/doc/scipy/reference/sparse.html))
# * Statistics ([scipy.stats](http://docs.scipy.org/doc/scipy/reference/stats.html))
# * Image processing ([scipy.ndimage](http://docs.scipy.org/doc/scipy/reference/ndimage.html))
# * IO (input/output) ([scipy.io](http://docs.scipy.org/doc/scipy/reference/io.html))
##

# %%
from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt


# ## Integration
#
# ### Numerical integration
#
# Numerically evaluating
#
# $\displaystyle \int_a^b f(x) dx$
#
# is called quadrature (abbr. quad). SciPy provides various methods for that:
# e.g., `quad`, `dblquad` and `tplquad` for simple, double or triple integrals.

# %%
from scipy.integrate import quad, dblquad, tplquad
# quad?


# Define a f function
def f(x):
    return x


a, b = 1, 2

val, abserr = quad(f, a, b)  # Integral between a and b

print("Integral =", val, ", Error =", abserr)

# dblquad?


# Double integral example:

# $\int_{x=1}^{2} \int_{y=1}^{x} (x + y^2) dx dy$

# %%

def f(y, x):
    return x + y**2


def gfun(x):
    return 1


def hfun(x):
    return x


print(dblquad(f, 1, 2, gfun, hfun))


# ### Ordinary differential equation (ODE)
#
# SciPy provides two ways for solving ODE:
# 1) an API with `odeint`,
# 2) an object-oriented API with `ode`.
#
# `odeint` is simpler, we will only use that one here.
#
# Import:
from scipy.integrate import odeint
# %%


# An ODE system can be written :
#
# $y' = f(y, t)$
#
# with
#
# $y = [y_1(t), y_2(t), ..., y_n(t)]$
#
# and $f$ a function the provides the derivatives of $y_i(t)$. To solve an ODE
# you need to specify $f$ and the initial conditions, $y(0)$.
#
# Once defined, you can use `odeint`:
#     y_t = odeint(f, y_0, t)
#
# where `t` is a NumPy *array* of coordinates at which you aim to solve
# the ODE, `y_t` is a NumPy *array* with a line for each time `t`; each column
# corresponds to the solution `y_i(t)`.

# #### Example: double pendulum

# Description: http://en.wikipedia.org/wiki/Double_pendulum

# %%
from IPython.core.display import Image
Image(url='http://upload.wikimedia.org/wikipedia/commons/c/c9/Double-compound-pendulum-dimensioned.svg')


# The double pendulum equations are available on wikipedia:
#
# ${\dot \theta_1} = \frac{6}{m\ell^2} \frac{ 2 p_{\theta_1} - 3 \cos(\theta_1-\theta_2) p_{\theta_2}}{16 - 9 \cos^2(\theta_1-\theta_2)}$
#
# ${\dot \theta_2} = \frac{6}{m\ell^2} \frac{ 8 p_{\theta_2} - 3 \cos(\theta_1-\theta_2) p_{\theta_1}}{16 - 9 \cos^2(\theta_1-\theta_2)}.$
#
# ${\dot p_{\theta_1}} = -\frac{1}{2} m \ell^2 \left [ {\dot \theta_1} {\dot \theta_2} \sin (\theta_1-\theta_2) + 3 \frac{g}{\ell} \sin \theta_1 \right ]$
#
# ${\dot p_{\theta_2}} = -\frac{1}{2} m \ell^2 \left [ -{\dot \theta_1} {\dot \theta_2} \sin (\theta_1-\theta_2) +  \frac{g}{\ell} \sin \theta_2 \right]$
#
# where $p_{\theta_i}$ are moments of inertia.
# To simplify the Python code, you can use the variable $x = [\theta_1, \theta_2, p_{\theta_1}, p_{\theta_2}]$
#
# ${\dot x_1} = \frac{6}{m\ell^2} \frac{ 2 x_3 - 3 \cos(x_1-x_2) x_4}{16 - 9 \cos^2(x_1-x_2)}$
#
# ${\dot x_2} = \frac{6}{m\ell^2} \frac{ 8 x_4 - 3 \cos(x_1-x_2) x_3}{16 - 9 \cos^2(x_1-x_2)}$
#
# ${\dot x_3} = -\frac{1}{2} m \ell^2 \left [ {\dot x_1} {\dot x_2} \sin (x_1-x_2) + 3 \frac{g}{\ell} \sin x_1 \right ]$
#
# ${\dot x_4} = -\frac{1}{2} m \ell^2 \left [ -{\dot x_1} {\dot x_2} \sin (x_1-x_2) +  \frac{g}{\ell} \sin x_2 \right]$

# %%
g = 9.82
L = 0.5
m = 0.1


def dx(x, t):
    """The right-hand side of the pendulum ODE."""
    x1, x2, x3, x4 = x[0], x[1], x[2], x[3]

    dx1 = 6.0/(m*L**2) * (2 * x3 - 3 * np.cos(x1-x2) * x4) / \
        (16 - 9 * np.cos(x1-x2)**2)
    dx2 = 6.0/(m*L**2) * (8 * x4 - 3 * np.cos(x1-x2) * x3) / \
        (16 - 9 * np.cos(x1-x2)**2)
    dx3 = -0.5 * m * L**2 * \
        (dx1 * dx2 * np.sin(x1-x2) + 3 * (g/L) * np.sin(x1))
    dx4 = -0.5 * m * L**2 * (-dx1 * dx2 * np.sin(x1-x2) + (g/L) * np.sin(x2))

    return [dx1, dx2, dx3, dx4]


# %%

# Choose an initial condition
x0 = [np.pi/4, np.pi/2, 0, 0]

# Discretize from 0 to 10 seconds
t = np.linspace(0, 10, 200)
n_point = len(t)
# Solve
x = odeint(dx, x0, t)
print(x.shape)


# %%
# Display
from celluloid import Camera

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].plot(t, x[:, 0], 'r', label="$\\theta_1$")
axes[0].plot(t, x[:, 1], 'b', label="$\\theta_2$")
axes[0].set_title("Angular evolution")
axes[0].legend(loc='upper right')

x1 = + L * np.sin(x[:, 0])
y1 = - L * np.cos(x[:, 0])
x2 = x1 + L * np.sin(x[:, 1])
y2 = y1 - L * np.cos(x[:, 1])

axes[1].plot(x1, y1, 'r', label="pendulum1")
axes[1].set_ylim([-1, 0])
axes[1].set_xlim([1, -1])
axes[1].set_title("Space evolution")
alphas = np.linspace(0, 1, n_point)
for i in range(len(t)-1):
    axes[1].plot(x2[i:i+2], y2[i:i+2], '-', color='blue', alpha=alphas[i])
    axes[1].plot(x1[i], y1[i], '.', color='red', label="pendulum1")
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.001)

plt.show()
# ### <font color='red'> EXERCISE : alpha and time </font>
# Modify the code above so that on the right plot the older points in time are
# more transparent than the new ones.

# ## Linear algebra
#
# SciPy for Linear algebra : use `linalg`. It includes function for solving
# lineair systems, eigen value decomposition, SVD,
# Gaussian elimination (LU, Cholesky), etc.
#
# Documentation : http://docs.scipy.org/doc/scipy/reference/linalg.html

# #### Solving linear systems:
#
# Find x such that:
#
# $A x = b$
#
# for specified matrix $A$ and vector $b$.

# %%s
# A = np.array([[1, 0, 3], [4, 5, 12], [7, 8, 9]], dtype=np.float)
A = np.random.randn(500, 500)
b = np.ones((500, 1))
# A = np.array([[1, 0, 3], [4, 5, 12], [7, 8, 9]], dtype=np.float)
# b = np.array([[1, 2, 3]], dtype=np.float).T
# b = np.array([[1, 2, 3]], dtype=np.float).T

print(A)
print(b)

# %%

x = linalg.solve(A, b)
print(x)
print(x.shape)
print(b.shape)

# %%

# Check the result at given precision (different from ==)
np.allclose(A @ x, b, atol=1e-14, rtol=1e-15)

# **Remark**: NEVER (or you should really know why) invert a matrix.
# **ALWAYS** solve linear systems instead!

# #### Eigen values / vectors

# $\displaystyle A v_n = \lambda_n v_n$
#
# with $v_n$ the $n$-th eigen vector and  $\lambda_n$ the $n$-th eigen value.
#
# `eigvals` abd `eig`

# %%

A = np.random.randn(3, 3)
A = A + A.T
evals, evecs = linalg.eig(A)
print(evals, '\n ------\n', evecs)

# V = [v_1, ... v_n] , columns = eigen vectors
# A = V diag(s_1,...,s_n) V^T

np.allclose(A, evecs @ np.diag(evals)@evecs.T)

# ### <font color='red'> EXERCISE : Eigen values/vectors</font>
#
#
# Verify numerically that the output from linalg.eig are indeed approximately
# eigen values and eigen vectors of the matrix A above.
#
# *Hint* : use https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html

# If A is symmetric you **should** use `eigvalsh` (H for Hermitian) instead:
# this is more robust, and leverages the structures (you know they are real!)

# %%
evals = linalg.eigvalsh(A)  # check evals, _ = linalg.eigh(A) also
print(evals)
print('----')
print(linalg.eigh(A))

# #### Matrix operations
# %%


linalg.inv(A)  # Inversion, consider NEVER using it though  :)
linalg.det(A)  # determinant

# normes
print(linalg.norm(A, ord='fro'))  # fro for Frobenius
print((np.sum(A**2))**0.5)
print(linalg.norm(A, ord=2))
print((linalg.eigvalsh(A.T@A)**0.5))
print(linalg.norm(A, ord=np.inf))


# ### <font color='red'> EXERCISE : Norms computation</font>
# Check numerically what is the instruction  `linalg.norm(A, ord=np.inf)`
# really computing.
# Double check with the help, and a numerical test.
# %%
A = np.random.randn(3, 3)
print(linalg.norm(A, ord=np.inf))

print(np.max(np.sum(np.abs(A), axis=1)))

# ## Optimization
#
# **Goal**: find functions minima or maxima
#
# Doc : http://scipy-lectures.github.com/advanced/mathematical_optimization/index.html
#
from scipy import optimize

# ### Find a (local!) minima;
# %%


def f(x):
    return 4*x**3 + (x-2)**2 + x**4


def mf(x):
    return -(4*x**3 + (x-2)**2 + x**4)



# %%
xs = np.linspace(-5, 3, 100)
plt.figure()
plt.plot(xs, f(xs))
plt.show()

#%%
#
# `fmin_bfgs` (see https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm)

x_min = optimize.fmin_bfgs(f, x0=-4)
x_max = optimize.fmin_bfgs(mf, x0=-2)
x_min2 = optimize.fmin_bfgs(f, x0=2)


plt.figure()
plt.plot(xs, f(xs))
plt.plot(x_min, f(x_min), 'o', markersize=10, color='orange')
plt.plot(x_min2, f(x_min2), 'o', markersize=10, color='red')
plt.plot(x_max, f(x_max), '|', markersize=20)
plt.show()

# %%
x_argmins = np.zeros(xs.size)
x = optimize.fmin_bfgs(f, x0=-4)
mask = np.zeros(xs.size)

# Correction: with loops
plt.figure()
plt.plot(xs, f(xs))
for i in range(len(xs)):
    x_argmins[i]=optimize.fmin_bfgs(f, x0=xs[i], disp=False)
    if np.isclose(x_argmins[i], x_min)[0]:
        plt.plot(xs[i], f(xs[i]),
                 'o', markersize=10, color='orange')
    else:
        plt.plot(xs[i], f(xs[i]),
                 'o', markersize=10, color='red')
plt.plot(x_max, f(x_max), '|', markersize=50)


# ### <font color='red'> EXERCISE : Bassin of attraction</font>
#
# Draw the points on the curves with 2 different colors :
# - orange for the points leading to find the left local minima
# - red for the points leading to the right local minima.

#%%

# ### Find the zeros of a function
#
# Find $x$ such that $f(x) = 0$, with `fsolve`.
omega_c = 3.0


def f(omega):
    return np.tan(2*np.pi*omega) - omega_c / omega


# %%
x = np.linspace(1e-8, 3.2, 1000)
y = f(x)
mask = np.where(np.abs(y) > 50)
x[mask] = y[mask] = np.nan  # remove vertical line when the function flips sign 
plt.plot(x, y)
plt.plot([0, 3.3], [0, 0], 'k')
plt.ylim(-5, 5)


# %%
optimize.fsolve(f, 0.72)
optimize.fsolve(f, 1.1)
optimize.fsolve(f, np.linspace(0.001, 3, 20))
np.unique(np.round(optimize.fsolve(f, np.linspace(0.2, 3, 20)), 3))

# %%
my_zeros = np.unique(
    (optimize.fsolve(f, np.linspace(0.2, 3, 20)) * 1000).astype(int)) / 1000.
plt.figure()
plt.plot(x, y, label='$f$')
plt.plot([0, 3.3], [0, 0], 'k')
plt.plot(my_zeros, np.zeros(my_zeros.shape), 'o', label='$x : f(x)=0$')
plt.legend()
plt.show()


# #### Parameters estimation

# %%
from scipy.optimize import curve_fit


def f(x, a, b, c):
    """f(x) = a exp(-bx) + c."""
    return a * np.exp(-b * x) + c


x = np.linspace(0, 4, 50)
y = f(x, 2.5, 1.3, 0.5)  # true signal
yn = y + 0.2*np.random.randn(len(x))  # noisy added


# %%
plt.figure()
plt.plot(x, yn, '.')
plt.plot(x, y, 'k', label='$f$')
plt.legend()


# %%
(a, b, c), _ = curve_fit(f, x, yn)
print(a, b, c)

# %%

# curve_fit?

# Display:

# %%
plt.figure()
plt.plot(x, yn, '.', label='data')
plt.plot(x, y, 'k', label='True $f$')
plt.plot(x, f(x, a, b, c), '--k', label='Estimated $\hat{f}$')
plt.legend()
plt.show()


# For polynomial you can directly use `numpy`

# %%

x = np.linspace(0, 1, 10)
y = np.sin(x * np.pi / 2.)
line = np.polyfit(x, y, deg=10)
plt.figure()
plt.plot(x, y, '.', label='data')
plt.plot(x, np.polyval(line, x), 'k--', label='polynomial approximation')
plt.legend()
plt.show()
# xx = np.linspace(-5,4,100)
# plt.plot(xx, np.polyval(line,xx), 'g')


# ## Interpolation

# %%
from scipy.interpolate import interp1d

# %%


def f(x):
    return np.sin(x)


# %%

n = np.arange(0, 10)
x = np.linspace(0, 9, 100)

y_meas = f(n) + 0.1 * np.random.randn(len(n))  # add noise
y_real = f(x)

linear_interpolation = interp1d(n, y_meas)
y_interp1 = linear_interpolation(x)

cubic_interpolation = interp1d(n, y_meas, kind='cubic')
y_interp2 = cubic_interpolation(x)


# %%

# BarycentricInterpolator??


# %%

plt.figure()
plt.plot(n, y_meas, 'bs', label='noisy data')
plt.plot(x, y_real, 'k', lw=2, label='true function')
plt.plot(x, y_interp1, 'r', label='linear interp')
plt.plot(x, y_interp2, 'g', label='cubic interp')
plt.legend(loc=3)
plt.show()


# ### Images

# %%

from scipy import ndimage, misc
img = misc.face()
type(img), img.dtype, img.ndim, img.shape


# %%

2**8  # uint8-> code sur 256 niveau.


# %%

n_1, n_2, n_3 = img.shape
np.unique(img)


# %%
# ### True image
plt.figure()
plt.imshow(img)
plt.axis('off')
plt.show()


# %%
# ### RGB decomposition

fig, ax = plt.subplots(3, 2)
fig.set_size_inches(9, 6.5)
n_1, n_2, n_3 = img.shape

ax[0, 0].imshow(img[:, :, 0], cmap=plt.cm.Reds)
ax[0, 1].hist(img[:, :, 0].reshape(n_1 * n_2), np.arange(0, 256))

ax[1, 0].imshow(img[:, :, 1], cmap=plt.cm.Greens)
ax[1, 1].hist(img[:, :, 1].reshape(n_1 * n_2), np.arange(0, 256))

ax[2, 0].imshow(img[:, :, 2], cmap=plt.cm.Blues)
ax[2, 1].hist(img[:, :, 2].reshape(n_1 * n_2), np.arange(0, 256))

plt.tight_layout()


# %%

print(img.flags)  # cannot edit...
img_compressed = img.copy()
img_compressed.setflags(write=1)
print(img_compressed.flags)  # can edit now

# %%

img_compressed[img_compressed < 70] = 50
img_compressed[(img_compressed >= 70) & (img_compressed < 110)] = 100
img_compressed[(img_compressed >= 110) & (img_compressed < 180)] = 150
img_compressed[(img_compressed >= 180)] = 200
plt.figure()
plt.imshow(img_compressed, cmap=plt.cm.gray)
plt.axis('off')
plt.show()

### Convert a color image in grayscale

# %%

plt.figure()
plt.imshow(np.mean(img, axis=2), cmap=plt.cm.gray)
plt.show()


# Blurring (fr: floutage)

# %%

img_flou = ndimage.gaussian_filter(img, sigma=2)
plt.figure()
plt.imshow(img_flou, cmap=plt.cm.gray)
plt.axis('off')
plt.show()


# ### <font color='red'> EXERCISE : Color</font>
# Change the color of the flag to make it frenchier (e.g. use blue, white, red)
# or italianer (use red/white/green)
# %%

img = (255 * plt.imread('https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/486px-Flag_of_Brazil.svg.png')).astype(np.int)

plt.figure()
plt.imshow(img)
plt.show()


# %%

fig, ax = plt.subplots(3, 2)
fig.set_size_inches(9, 6.5)
n_1, n_2, n_3 = img.shape

ax[0, 0].imshow(img[:, :, 0], cmap=plt.cm.Reds)
ax[0, 1].hist(img[:, :, 0].reshape(n_1 * n_2), np.arange(0, 256), density=True)

ax[1, 0].imshow(img[:, :, 1], cmap=plt.cm.Greens)
ax[1, 1].hist(img[:, :, 1].reshape(n_1 * n_2), np.arange(0, 256), density=True)

ax[2, 0].imshow(img[:, :, 2], cmap=plt.cm.Blues)
ax[2, 1].hist(img[:, :, 2].reshape(n_1 * n_2), np.arange(0, 256), density=True)

plt.tight_layout()


# %%

# ### <font color='red'> EXERCISE : Make the Brazilian italianer</font>
# (green white red)

# XXX TODO
# colors levels

# %%
img = (255 * plt.imread('https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/486px-Flag_of_Brazil.svg.png')).astype(np.int)
img = img.copy()
plt.figure()
plt.imshow(img[:, :, 2], cmap=plt.cm.gray)

# %%
find_white_green = img[:, :, 1] > 200
find_light_green = (img[:, :, 1] <= 200)*(img[:, :, 1] > 50)
find_dark_green = img[:, :, 1] <= 50

# red part
img[:, :, 0][find_dark_green] = 255
img[:, :, 1][find_dark_green] = 0
img[:, :, 2][find_dark_green] = 0

#  white part
img[:, :, 0][find_white_green] = 255
img[:, :, 1][find_white_green] = 255
img[:, :, 2][find_white_green] = 255

# blue part
img[:, :, 0][find_light_green] = 0
img[:, :, 1][find_light_green] = 0
img[:, :, 2][find_light_green] = 255

plt.imshow(img)
plt.show()

# # More for colors/ images:
# http://josephsalmon.eu/enseignement/Montpellier/HLMA310/matplotlib_slides.pdf
#


# ## Further lectures
#
# * http://www.scipy.org - The official web page for the SciPy project.
# * http://docs.scipy.org/doc/scipy/reference/tutorial/index.html - A tutorial on how to get started using SciPy.
# * https://github.com/scipy/scipy/ - The SciPy source code.
# * http://scipy-lectures.github.io
#
