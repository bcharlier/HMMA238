#!/usr/bin/env python

# coding: utf-8

# # `numpy`  multi-dim arrays) and `matplotlib` (visualization 2D / 3D)
#
#       Joseph Salmon : joseph.salmon@umontpellier.fr
#
# Adapted from the work by
#
# - A. Gramfort (alexandre.gramfort@inria.fr) http://alexandre.gramfort.net/
# - J.R. Johansson (robert@riken.jp) http://dml.riken.jp/~rob/

# See also:
# - https://github.com/rougier/numpy-tutorial (short version + cheatsheet)
# - https://www.labri.fr/perso/nrougier/from-python-to-numpy/ (long version)

# ## Introduction

# * `numpy` is a module used in almost all numerical computation projects with
# `Python`.
# It provides powerful data structures for the manipulation of more general
# vectors, matrices and tensors.
# * `numpy` is written in `C` and `Fortran` hence its high performance when
# calculations are vectorized, i.e., formulated as vector/matrix operations.

# * `matplotlib` is a powerful module for generating 2D and 3D graphics.
# * syntax very close to Matlab
# * supports text and $\LaTeX$ labels
# * quality outputs for various formats (.png, .pdf, .svg, .gif, etc.)
# * interactive graphical user interface to explore the figures (using widget,
#   possibly with notebooks)


# %%
# Let us first load `numpy` and `matplotlib`:

import numpy as np  # usual shortcut
import matplotlib.pylab as plt  # usual shortcut


# ## *Arrays* in `numpy`
#
# In `numpy`, vectors, matrices and other multi-dimensional tensors
# (arrays with more than 2 dimensions) are called *arrays*.
#

# ## Creating  `numpy` *arrays*
#
# Several possibilities are offered:
#
#  * transform `Python` lists or n-uplets
#  * use a dedicated function, such as `arange`, `linspace`, etc.
#  * load a file

# ### `numpy` *arrays* from lists
# Use simply the `numpy.array` command:

# %%


# Creating a vector from a list
v = np.array([1, 3, 2, 4])
print(v)
print(type(v))


# Let us visualize this vector with `matplotlib`:

# %%

x = np.array([0, 1, 2, 3])

fig = plt.figure(figsize=(5,2))
plt.plot(x, v, 'rv--', label='v(x)')
# r for red, v for triangle, -- for dash line
plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('v')

plt.title('Mon titre')

plt.xlim([-1, 4])
plt.ylim([-10, 5])

plt.show()  # to force the display
fig.savefig('toto.pdf')  # uncomment to save on disk


# ###  Create matrices / 2-d `numpy` arrays from a list of lists

# %%
M = np.array([[1, 2], [3, 4]])
print(M)
print(M[1, 1])

# The objects `v` and `M` are of type `ndarray` (the `numpy` standard format)

# %%

type(v), type(M)

# `v` and `M` have different shapes :

# %%

v.shape  # note that second dimension is empty for a vector !!!


# %%

n = v.shape
n[0]


# %%

M.shape


# To get the number of element in an *array* :

# %%

v.size


# %%

M.size


# Alternatively use: `np.shape` and `np.size`

# %%

np.shape(M)


# *arrays* have a type obtained by typing `dtype`:

# %%

print(M)
print(M.dtype)


# Types must be respected when handling *arrays*. Check what follows:

# %%

M[0, 0] = "hello"


# ### `numpy` *arrays* `dtype` is fixed

# %%

a = np.array([1, 2, 3])
a[0] = 3.2
print(a)
a.dtype


# %%

a = np.array([1, 2, 3], dtype=np.int64)
b = np.array([0, 1, 1], dtype=np.int64)
b = b.astype(bool)
print(a / b)


# You can force the type explicitely using the `dtype` argument:

# %%

M = np.array([[1, 2], [3, 4]], dtype=complex)
M


#  * Other possible types `dtype` :
#    `int`, `float`, `complex`, `bool`, `object`, etc.
#
#  * The bit precision can be specified:
#    `int64`, `int16`, `float128`, `complex128`.
#
# See possible types here:
# https://docs.scipy.org/doc/numpy/user/basics.types.html

# ###  `numpy` *arrays* deterministically generated

# #### `arange`

# %%

# Create a simple interval
x = np.arange(0, 9, 2)  # arguments: start, stop, step
x


# %%

x = np.arange(-1, 1, 0.1)
x


# #### `linspace` and `logspace`

# %%

# Beware : the end IS INCLUDED with `linspace`
np.linspace(0, 10, 25)


# %%

np.linspace(0, 10, 11)


# %%

xx = np.linspace(-10, 10, 100)
fig = plt.figure(figsize=(5, 5))
plt.plot(xx, np.sin(xx))
plt.show()

# %%

logarray = np.logspace(1, 1000, 3)
np.log(logarray)


# %%

(np.logspace(1, 10, num=10, base=2))


# %%

np.logspace?
# %%

print(np.logspace(0, 10, num=10, base=np.e))

# ### <font color='red'> EXERCISE : log/exp </font>
# What is the value 3.03777 corresponding to ?

# #### `diag`

# %%

# Diagonal matrix
A = np.diag([1, 2, 3])
A[1, 2] = 17
A
np.diag(A)


# %%

# Diagonal matrix with a shift on the diagonal
np.diag([1, 2, 3], k=1)


# %%

# np.diag?
my_diag = np.array([0, 0, 0])
print(my_diag.shape)
print(M.shape)
np.diag(my_diag)
np.fill_diagonal(, my_diag)
print(M)


#
# This function also extract the diagonal value of an *array* :

# %%

print(A)
print(np.diag(A))


# %%

np.diag(A, k=-3)


# #### `zeros`, `ones` and  `full`

# %%

np.zeros((3,), dtype=int)  # beware zeros(3, 3) produces an error
print(np.zeros((3,), dtype=int).dtype)


# %%

zero_mat_float = np.zeros((2, 3, 5))

print(zero_mat_float.dtype)
print(zero_mat_float)
zero_mat_float.shape
zero_mat_float[1, :, :]


# %%

np.ones((3,)).shape


# %%

print(np.zeros((3,), dtype=int))
print(np.zeros((1, 3), dtype=int))
print(np.zeros((3, 1), dtype=int))


# %%

np.full((5, 4), 9)


# ### `numpy` *array* (pseudo)-randomly generated

# %%

# uniform at random in [0,1] samples
np.random.rand(5, 5)


# %%

# normal random samples
np.random.randn(5, 5)  # n stands for normal here


# Rem: cf. scipy.stats for more on random generators

# #### Random seed
# It is often useful to "fix" the way the randomness is generated:
# https://fr.wikipedia.org/wiki/Graine_al%C3%A9atoire

# %%

np.random.rand(12)


# Now the result is always the same for a fixed seed (fr: *graine*), even
# when re-executing the command multiple times:

# %%

np.random.seed(seed=33)
print(np.random.rand(12))
print(np.random.rand(12))
print(np.random.rand(12))

# %%
np.random.seed(seed=33)
print(np.random.rand(12))

np.random.seed(seed=33)
print(np.random.rand(12))

np.random.seed(seed=33)
print(np.random.rand(12))

# #### Histograms for random samples

# %%

a = np.random.normal(loc=0.0, scale=1., size=(10000,))
b = np.random.normal(loc=0.0, scale=10., size=(10000,))  # scale =  std

plt.figure(figsize=(5, 2))

plt.subplot(1, 3, 1)
plt.hist(a, bins=40, density=True)
plt.title('Histogram \n (Sample size)')
plt.ylabel('Sample size')

plt.subplot(1, 3, 2)
plt.hist(10 * a, bins=40, density=True)
plt.title('Histogram \n (Density)')
plt.ylabel('Density')

plt.subplot(1, 3, 3)
plt.hist(b, bins=40, density=True)
plt.title('Histogram \n (Density)')
plt.ylabel('Density')

plt.tight_layout()  # avoid axes display issues...matplotlib might be tricky


# %%

import matplotlib
matplotlib.__version__


# %%

fig, axes = plt.subplots(2, 1, sharex='col')

axes[0].hist(a, bins=40, density=False)
axes[0].set_ylabel('Sample size')
axes[0].set_title('Histogram (Sample size)')

axes[1].hist(a + 10, bins=40, density=True)
axes[1].set_ylabel('Density')
axes[1].set_title('Histogram (Density)')

plt.tight_layout()

# %%
fig, axes = plt.subplots(1, 2, sharey='row')

axes[0].hist(a, bins=40, density=True)
axes[0].set_ylabel('Sample size')
axes[0].set_title('Histogram (Sample size)')

axes[1].hist(a + 10, bins=40, density=False)
axes[1].set_title('Histogram (Density)')

plt.tight_layout()


# ##  Input/Output files

# ### `numpy` default/recommended storing format  (`.npy`)
#
# To save and load `numpy` *arrays* : `numpy.save` and `numpy.load` :

# %%

M = np.random.rand(3, 3)
print(M)
np.save("random-matrix.npy", M)
!cat random-matrix.npy


# ### CSV`
# You can use CSV (Comma-Separated Values), but this is rather uncommon, with
# `numpy`, it is way more common with pandas `though`

# To save into a csv file (or a text file) `numpy.savetxt`:

# %%

np.savetxt("random-matrix.csv", M)


# %%
!pwd  # check the new file in your folder
!ls
# to read from a txt file: `numpy.genfromtxt`,

# %%

MM = np.genfromtxt('random-matrix.csv')  # create an array from a csv file
print(MM)

# *Remark*: you might loose some precision when doing the storage,
# if not careful.


# %%

N = np.load("random-matrix.npy")
print(N)


# ## Other properties of `numpy` *arrays*

# %%

M


# %%

M.dtype


# %%

M.itemsize  # byte by element


# %%

# bytes (fr:octets), see https://fr.wikipedia.org/wiki/Byte
np.random.randn(1000, 1000).nbytes


# **Remark**: the memory footprint of an array can change with its type.

# %%

MM = np.random.randn(1000, 1000).astype(np.int8)
MM.nbytes


# %%

print("{} bytes".format(M.size * M.itemsize))


# %%

M.nbytes / M.size


# %%

M.ndim  # number of dimensions


# %%

print(np.zeros((3,), dtype=int).shape)
print(np.zeros((1, 3), dtype=int).shape)
print(np.zeros((3, 1), dtype=int).shape)
print(np.zeros((3, 2, 3), dtype=int).shape)


# %%

print(np.zeros((3,), dtype=int).ndim)
print(np.zeros((1, 3), dtype=int).ndim)
print(np.zeros((3, 1), dtype=int).ndim)
print(np.zeros((3, 2, 3, 6), dtype=int).ndim)


# ##  *arrays* manipulation

# ### Indexation

# %%

# v is a vector: one dimension / index
v[3]


# %%

# M is a matrix or a 2D array : two dimensions / indices
M[1, 1]

# %%

# Extract lines / columns:

# %%

M[:, 1]  # 2nd column
M[:, 2]  # 3rd column


# %%

print(M.shape)
print(M[1, :].shape, M[:, 1].shape)


# Update a matrix entry

# %%

M[0, 0] = 1
print(M)

# %%

# extract / affect lines
M[1, :] = -1
print(M)


# %%

M[1, :] = [1, 2, 3]
print(M)

# ## *Slicing*
#
# *Slicing* syntax: `M[start:stop:step]` to extract a sub part of an *array*

# %%

A = np.array([1, 2, 3, 4, 5])
A


# %%

A[1:3]


# Slices can be modified :

# %%

A[1:3] = [-2, -3]
A


# You can omit any of the start/stop/step argument in `M[start:stop:step]`:

# %%

A[::]
A[:]

# %%

A[::2]  # stepsize = 2


# %%

A[:3]  # the first 3 elements


# %%

A[3:]  # that last elements, starting from the 4th

# %%

np.arange(12)


# %%
# Ordering convention in arrays:

M = np.arange(12).reshape(4, 3, order='F')  # F stands for Fortran convention
print(M)
M = np.arange(12).reshape(4, 3, order='C')  # F stands for C convention
print(M)
M = np.arange(12).reshape(4, 3)  # C order by default
print(M)

# difference in time
# %%
import time
# do stuff
n_rows, n_cols = 10000, 10000
big_m = np.random.rand(n_rows, n_cols)

# Variant 1: C order (lines)
big_m_c = np.ascontiguousarray(big_m)
t = time.time()
for i in range(n_cols):
        np.sum(big_m[:, i]**2)
print("C:", time.time() - t)

# Variant 2: Fortran order (columns)
big_m_f = np.asfortranarray(big_m)
t = time.time()
for i in range(n_cols):
        np.sum(big_m_f[:, i]**2)
print("F:", time.time() - t)

# %%
A = np.array([1, 2, 3, 4, 50])
A[-1]  # last index
A[:-1]  # negative indexes
A[-3:]   # last 3 indexes


# ### <font color='red'> EXERCISE : finite differencing </font>
# Compute the finite differencing of $A$, i.e., the vector $A[k+1]-A[k]$
# for $k=0, \dots,n-1$ (where $n$ is the length of A).
# Remark: this is often used to perform derivatives approximations.
# You can check your solution with the specific `numpy` function `np.diff`.
# *slicing* works similarly for multi-dimensional *array*.

# %%

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
A


# %%

A[1:4, 1:4]  # sub-array


# %%

# every 3 row/column:
A[::3, ::3]


# %%

A


# %%

print(A[[0, 1, 3]])
print(A[[0, 1, 3], :])
print(A[:, [0, 1, 3]])


# ### <font color='red'> EXERCISE : slicing / vectorization </font>
#
# Create a $6 \times 6$ matrix where the integers from 1 to 36 are stored
# (in column ordering / Fortran ordering).
# Then, substitute all even number by 0, **without using a loop**.

# %%
# Transpose: 2 ways for that
print(np.transpose(np.arange(1, 37).reshape(6, 6)))
print((np.arange(1, 37).reshape(6, 6)).T)

# ### *fancy indexing*

# %%

row_indices = [1, 2, 3]
print(A)
print(A[row_indices])
print(A.shape)
print(A[[1, 2], [3, 4]])


# %%

A[np.ix_([1, 2], [3, 4])] = 0
print(A)


# Using a binary mask:
# %%

B = np.arange(5)
print(B)


# %%

row_mask = np.array([True, False, True, False, False])
print(B[row_mask])


# %%

# equivalently
row_mask = np.array([1, 0, 1, 0, 0], dtype=bool)
B[row_mask]


# %%
a = np.array([1, 2, 3, 4, 5])
print(a < 3)
# %%
print(a[a <= 3])

# %%

print(A)
# %%

print(a < 3)
print(A[:, a < 3])


# ## Extract data from *arrays* and *array* creation

# #### `where`
#
# convert mask with `where`

# %%

x = np.arange(0, 10, 0.5)
print(x)
mask = (x > 5) * (x < 7.5)
print(mask)
y = (np.random.randn(len(x)))
print(y)
indices = np.where(mask)
print(indices)
print(y[indices])

# %%

print(x[indices])  # équivalent à x[mask]
print(x[mask])

# ## Use conditions and `arrays`
#
# `any`, `all` (not Annie Hall!)

# %%

if (M > 5).any():
    print("at least one element of M is > 5.")
else:
    print("no element of M is > 5.")


# %%

if (M > 5).all():
    print("all elements of M are > 5.")
else:
    print("there exist one element at least < 5.")




# ## Linear algebra
#
# The performance of programs written in `Python/numpy` depends on the ability
# to vectorize calculations (write them as operations on vectors/matrices)
# avoiding `for/while` loops as much as possible.
#
# ### Scalar operations
#
# Standard arithmetic operations with scalars (add, multiply, etc.):

# %%

v1 = np.arange(0, 5)
print(v1)


# %%

v1 * 2


# %%

v1 + 2


# %%

plt.figure(figsize=(8,4))
plt.subplot(1, 2, 1)
plt.plot(v1 ** 2, '--', color='blue', label=r'$y = x^2$')
plt.legend(loc=0)
plt.subplot(1, 2, 2)
plt.plot(np.sqrt(v1), '*-', color='red', label=r'$y = \sqrt{x}$')
plt.legend(loc=2)
plt.show()


# ### Term by term (Hadamard style operation)
#
# By default operation are elementwise (contrary to Matlab for instance).

# %%

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
print(A)


# %%

A * A  # element-wise multiplication
print(A**2)

# ### Matrix algebra
#
# Two ways for matrix multiplication :
#
#  * old ways: with `dot` (np.dot or A.dot(B))
#  * new way:  with `@/matmul`
#

# %%

print(np.dot(A, A))  # matrix / matrix multiplication
print(A.dot(A))  # matrix / matrix multiplication
print(A @ A)  # matrix / matrix multiplication
print(A * A)  # element-wise matrix / matrix multiplication
print(np.exp(A))

# %%
print(np.linalg.matrix_power(A, 3))
print(A @ A @ A)

# from scipy.linalg import expm
# expm(A)

# %%

v1
A.dot(v1)  # matrix / vector multiplication
np.dot(v1, v1)  # vectors inner product


# ### Transposition : Symmetric/anti-symmetric matrices

# %%
print(A)
S1 = (A + A.T) / 2  # orthogonal projection of A onto symmetric matrices
print(S1)

S2 = (A + np.transpose(A))/2
print(S2)
# %%

A1 = (A - A.T) / 2  # orthogonal projection of A onto anti-symmetric matrices
print(A1)
print(np.trace(A1))

# ### Orthogonality for the trace scalar product
#
# https://en.wikipedia.org/wiki/Inner_product_space#Real_matrices

# %%

print(A1 + S1)
np.trace(S1 @ A1)  # inner product (fr: "produit scalaire")


# %%

print(v1)
print(v1 * v1)


# %%

A.shape, v1.size


# %%
# Matrix vector operations
print(A)
print(v1)
print(A * v1)


# %%

n_samples = 300
C = np.random.rand(n_samples, 200)

D = np.dot(C.T, C)  # multiply C^T by C : C^T C
D = C.T@C  # idem multiply C^T by C : C^T C
D = C.T.dot(C)  # idem multiply C^T by C : C^T C


# ### <font color='red'> EXERCISE : *numpy* ninja </font>
#
# Without any loop (`for/while`)
#  * <font color='red'> Create  `Mat`:
# Mat = np.array([[n+m*10 for n in range(5)] for m in range(5)])
#    </font>
#  * <font color='red'> Replace every other column by its value minus the value
# of the following column (except for the last one). More precisely,
# starting from Mat = [C_1, C_2, C_3, C_4] (4 columns), one aims at creating
# NewMat = [C_1 - 2 C_2, C_2 - 2 C3, C_3 -2 C4, C_4]
# </font>
#  * <font color='red'> Replace the negative values by 0,
# using a binary mask.</font>

# %%

# Solution 1: for loops and columns operations
Mat = np.array([[n+m*10 for n in range(4)] for m in range(5)])
print(Mat)
NewMat = np.copy(Mat)
print("---------")
for j in range(4-1):
    NewMat[:, j] = Mat[:, j] - 2 * Mat[:, j+1]
print(NewMat)
# %%
print(NewMat)


# %%

# Solution 2: Transvection matrices
NewMat = Mat.copy()

# See on your own: `inner`, `outer`, `cross`, `kron`, `tensordot`.

# %%

# ### Matrix algebra
# #### Simple data analysis
#
# `numpy` propose functions to compute simple statistics:

# %%

data = np.vander([1, 2, 3, 4], increasing=True)  # Matrice de Vandermonde
print(data)


# #### `mean`

# %%

print(np.mean(data))
print(np.mean(data, axis=0))
print(np.mean(data, axis=1))


# %%

# column mean
np.mean(data[:, 2])


# ### <font color='red'> EXERCISE : On-line computation  of the mean </font>
# Write a recursive function computing the mean $\bar{x}_n$
# (without using `np.sum`,`np.mean` etc.).
#
# *Hint*:
#
# \begin{align}
# \bar{x}_{n} & = \frac{1}{n} \sum_{i=1}^{n} x_i \\
#             & = \frac{1}{n} \left( (n-1) \cdot \bar{x}_{n-1} + x_{n}\right)\\
#             & = \frac{1}{n} \left(\sum_{i=1}^{n-1} x_i  + x_{n} \right)\\
#             & = \frac{n-1}{n}  \cdot \bar{x}_{n-1}  + \frac{1}{n} x_{n}\\
# \end{align}

# #### Variance and standard deviation

# %%
print(np.var(data[:, 2]), np.std(data[:, 2]))
# ddof : Delta Degrees of Freedom
print(np.var(data[:, 2], ddof=1), np.std(data[:, 2], ddof=1))


# ### <font color='red'> EXERCISE : Degrees of Freedom </font>
# Explain the difference in behavior of the last cells.
# See more on this theme and on Stein's theory here:
# http://www.stat.cmu.edu/~larry/=sml/stein.pdf

# #### min / max / sum / prod

# %%

print(data[:, 2].min(), data[:, 2].max(),
      data[:, 2].sum(), data[:, 2].prod())


# %%

# cumsum
print(data[:, 2])
print(np.cumsum(data[:, 2]))
print(np.cumsum(data[:, 2]) / np.arange(1, len(data[:, 2]) + 1))

# %%

# cumprod
np.cumprod(data[:, 2]+1)


# %%

# equivalent to diag(A).sum()
np.trace(data)


# ### <font color='red'> EXERCISE : Wallis product (bis) </font>
# Using `numpy`, and without any `for` loop, visualize the quality of
# approximation using $n$ instead of +\infty
# \begin{align}
#     \text{Wallis product}\quad \pi&= 2 \cdot \prod_{n=1}^{\infty}
#     \left({\frac{4 n^{2}}{4 n^{2} - 1}}\right)
# \end{align}
# %%
n = 1000

# ### multi-dimensional computations
#
# Apply `min`, `max`, etc., row/column wise :

# %%

m = np.random.rand(3, 4)

# %%


m.max()  # max global
m.max(axis=0)  # max column wise
m.max(axis=1)  # max row wise

# ## Copy et "deep copy"
#
# For performance `numpy` don't copy objects by defaults, only pointer

# %%

A = np.array([[0,  2], [3, 4]])
print(A)
B = A
# %%
# ATTENTION: change B impacts A
B[0, 0] = 10
print(B)
print(A)
B = A
print(B is A)


# Use deep copy to avoid that

# %%

B = A.copy()  # same as B = np.copy(A)
# now modifying B, A is not affected.
print(B is A)
B[0, 0] = -5
print(B)
print(A)
print(B is A)

# %%

print(A - A[:, 0])
print(A - A[:, 0].reshape((2, 1)))


# ## Change size/reshape/concatenate
#

# %%

A


# %%

n, m = A.shape


# %%

B = A.reshape((1, n * m))
B


# %%

B[0, 0:5] = 5  # modify the array
B


# %%

A


# ### BEWARE !
#  B is simply a **view** of A.

# `flatten` from an array to a (flatten) vector
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flatten.html

# %%

A = np.array([[0,  2], [3,  4]])
B = A.flatten(order='F')
print(A, B)


# %%

B[0:5] = 10
B


# %%

A  # B is now a copy A


# ### Add another dimension with `newaxis`
#
# For instance to convert a vector in a line/column matrice:

# %%

v = np.array([1, 2, 3])
print(np.shape(v))

# %%

# Create a matrix with one column from the vector v
v[:, np.newaxis]


# %%

v[:, np.newaxis].shape


# %%

# Create a matrix with one line from the vector v
v[np.newaxis, :].shape


# ### Concatenate and repeat *arrays*
#
# Use `repeat`, `tile`, `vstack`, `hstack`, `concatenate` to create bigger
# matrices
#

# #### `repeat` amd `tile`

# %%

a = np.array([[1, 2], [3, 4]])
a


# %%

# Repeat each element 3 times
np.repeat(a, 3)

# %%

# Specify the `axis` argument
np.repeat(a, 3, axis=1)


# Repeat the matrix with `tile`

# %%

# Repeat the matrix 3 times

np.tile(a, 3)


# #### `concatenate`

# %%

b = np.array([[5, 6]])


# %%

np.concatenate((a, b), axis=0)


# %%

np.concatenate((a, b.T), axis=1)


# #### `hstack` et `vstack`

# %%

np.vstack((a, b))


# %%

np.hstack((a, b.T))


# ## WARNING: avoid iterating over *array* element with a loop
#
#  * this is slow, use instead vectorized operations.
#  * yet sometimes is too hard to avoid (consider `numba` for efficiency then)

# %%

vector = np.array([1, 2, 3, 4])

for coef in vector:
    print(coef)


# %%

M = np.array([[1, 2], [3, 4]])

for row in M:
    print("row", row)
    for element in row:
        print(element)


# Use enumerate with `arrays`:
# %%

for row_idx, row in enumerate(M):
    print("row_idx", row_idx, "row", row)

    for col_idx, element in enumerate(row):
        print("col_idx", col_idx, "element", element)

        # update the matrix M: square each element
        M[row_idx, col_idx] = element ** 2


# %%
M
# %%
# Exercise : test time execution M**2 vs. loop
n = 100
m = 10
M1 = np.ones((n, n))
M2 = np.eye(m)
# print(M1)
# print(M2)
M_test1 = np.kron(M1, M2)
M_test2 = np.kron(M2, M1)

print(M_test1)
print(M_test2)



# ## *Type casting*
#

# %%

M = np.array([[-1, 2], [0, 4]])
M.dtype


# %%

M2 = M.astype(float)
M2


# %%

M2.dtype


# %%

M3 = M.astype(bool)
M3


# ## 2D function visualization

# #### `mgrid` (meshgrid)

# %%

x, y = np.mgrid[0:5, 0:5]


# %%

x


# %%

y


# imshow : where it is starting.
# %%

plt.figure(figsize=(6, 6))

plt.subplot(2, 2, 1)
plt.imshow(x, origin='lower')
plt.colorbar()

plt.subplot(2, 2, 2)
plt.imshow(y, origin='lower')
plt.colorbar()

plt.subplot(2, 2, 3)
plt.imshow(x, origin='upper')
plt.colorbar()


plt.subplot(2, 2, 4)
plt.imshow(y, origin='upper')
plt.colorbar()

# EXERCISE : share colorbar for all subplots.

# %%
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(5, 4))
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.2)
Y = np.arange(-4, 4, 0.2)
XX, YY = np.meshgrid(X, Y)
R = np.sqrt(XX**2 + YY**2)
Z = np.sin(R)
ax.plot_surface(XX, YY, Z, rstride=1, cstride=1, cmap='viridis')


# %%

xx, yy = np.mgrid[-50:50, -50:50]

plt.figure(figsize=(3, 3))
z = 1j * yy + xx
plt.imshow(np.angle(z, deg=True).T,
           extent=[-50, 50, -50, 50], origin='lower')
plt.axis('on')
plt.colorbar()
plt.figure(figsize=(3, 3))
plt.imshow(np.abs(z), extent=[-50, 50, -50, 50])
plt.axis('on')
plt.colorbar()
plt.show()


# %%

C = np.random.rand(300, 200)
plt.figure()
plt.imshow(C)
plt.colorbar()
plt.show()


# %%

plt.figure()
plt.imshow(C.T @ C)
plt.colorbar()
plt.show()


# ### <font color='red'> EXERCISE : multivariate Gaussian distribution</font>
# Draw the density of a 2D Gaussian distribution.
#
# *Hint*: see
# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.multivariate_normal.html
#

# %%

# ## Bonus: locating a source of the code you run:
import inspect
import numpy as np
inspect.getfile(np.linalg.norm)


# %%

# ## Bonus: display the source of the code you run (2nd version)
inspect.getsourcelines(np.linalg.norm)


# %%

# ## Bonus: locating a source of the code you run:
get_ipython().run_line_magic('pinfo2', 'np.linalg.norm')


# ## Further reading:
# * http://numpy.scipy.org
# * http://scipy.github.io/old-wiki/pages/Tentative_NumPy_Tutorial.html
# * http://scipy-lectures.org/ - for advanced features (e.g., sparse matrices)
# * http://scipy.org/NumPy_for_Matlab_Users - guide migrating MATLAB users
