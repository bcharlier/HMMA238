# Symmetric matrix diagonalization

## Group affected: group 4

The goal of this project is to be able to produce videos and widget representing the evolution of a standard matrix diagonalization algorithm through its iterate, following the spirit in:

<https://twitter.com/salmonjsph/status/1207069666780360705>

## Rotation and diagonalization for symmetric matrices

In this section you have to implement the Jacobi algorithm to diagonalize a symmetric matrix. The details is provided here: <https://en.wikipedia.org/wiki/Jacobi_eigenvalue_algorithm>.

You will illustrate your algorithm by proposing a video that illustrate on a `20 x 20` matrix the evolution of the algorithm on a random symmetric matrix (explain how you propose to randomly sample symmetric matrices).

You will also display an analysis of the time computing when the size of the matrix increases.

## QR algorithm

In this section you have to implement the QR algorithm to diagonalize a symmetric matrix. The details are provided here: <https://en.wikipedia.org/wiki/QR_algorithm>, and perform a similar work as for the Jacobi case.

## Alternative method

Propose another algorithm to perform the numerical diagonalization of a matrix (without using `eig` or `eigh`).

## Sparse symmetric matrices

Perform a similar study as above to handle sparse matrices.
You will have to propose also a way to generate a sparse matrix of interest.
