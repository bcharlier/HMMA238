# TP - Numpy and Matplotlib

## Code to Debug

### Factorial function
The factorial of an array using numpy is not defined. To check, use :

    import numpy as np

    np.math.factorial(np.arange(3))

It will raise the following error :
> TypeError: only size-1 arrays can be converted to Python scalars

In the following, we propose to debug the function to compute a array of factorial.
For example, given the following array : array([0, 1, 2, 3, 4, 5]), we want to return the factorial array : array([1, 1, 2, 6, 24, 120]).

    def np_factorial_array(array):
        prod = 1
        fact_array = np.ones(length(array))
        for i in range(array):
            prod *= i
            fact_array[i] = prod
        return(prod)

Corrected version :

    def np_factorial_array(array):
        prod = 1
        fact_array = np.ones(len(array))
        for i in array:
            if i != 0:
                prod *= i
                fact_array[i-1] = prod
        return(fact_array)

## Exercices

### Exponential Function with Numpy

As for the previous TP, we are interested in wrote a function using only numpy array to compute the truncated exponential function.
You can check your function :

> np_trunc_exp(0, 10) == 1

> np_trunc_exp(1, 10) == 2.71828180

Tips : use the function np_factorial_array
Corrected Version :

    def np_trunc_exp(x,n):
        k = np.arange(n+1)
        fact = np_factorial_array(k)
        trunc_ = (x**k/fact).sum()
        return(trunc_)

