# TP - Introduction to Python

## Code to Debug

### Exponential Function
The exponential function as many definition, one of them use power series :

<!-- $$
e^x = \sum_{k=0}^\infty \dfrac{x^k}{k!}
$$ -->

<div align="center"><img src="../svg/rIJPh8Fp3Y.svg"/></div>


Obviously, we aren't able to compute the full sum, but we are able to computed a truncated one :

<!-- $$
e^x \approx \sum_{k=0}^n \dfrac{x^k}{k!}
$$ -->

<div align="center"><img src="../svg/C20HOIFCVc.svg"/></div>




We wrote the following function to compute the truncated exponential in function of x and n, using a for loop :

    from math import factorial

    def trunc_exp(x, n):
    sum = 0
    for k in n:
        sum += x^k / factorial(k)
    return(sum)

Once you have find the problem above, you can check your work with "trunc_exp(1, 5)". It must return "2.708333...".

Corrected version :

    def trunc_exp(x, n):
        sum_ = 0
        for k in range(n):
            sum_ += x ** k / factorial(k)
        return(sum_)




## Exercices
