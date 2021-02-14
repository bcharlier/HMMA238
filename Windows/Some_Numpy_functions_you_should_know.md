 **Numpy** is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, 
along with a large collection of high-level mathematical functions to operate on these arrays. In this file; I will present some useful 
numpy functions along with data science and artificial intelligence applications; that i hope it will be helpful for you! 

## 1. numpy.histogram:

The **numpy.histogram**(x,bins=10,range=None, normed=None,weights=None,density=None) computes the histogram of a set of data. 
The function returns 2 values: the first one is the frequency count, an the second is the bin edges(extremity.)
By default, the histogram method breaks up the data set into 10 bins. Notice that the x-axis labels do not match with the bin size. 
This can be fixed by passing in a xticks parameter, containing the list of the bin sizes. 

## 2. numpy.linspace: 

The **numpy.linspace**(start,stop,num=50,endpoint=True,retstep=False,dtype=None,axis=0) function returns evenly spaced numbers over 
a specified interval defined by the first two argulents of the function(start and stop --required arguments). The number of samples
generated is specified by the third argument num. If omitted, 50 samples are generated. One important thing to bear in mind while 
working with this function is that the stop element is provided in the returned array (by default endpoint=True), unlike in the built-in 
python function range. Linspace function can be used to generate evenly spaced samples for the x-axis. For instance, if we want to plot 
a mathematical function, we can easily generate samples for the x-axis by using the numpy.linspace function. 

## 3. numpy.repeat: 

The **numpy.repeat**(x, repeats,axis=None) function repeats the elements of an array. The number of repetitions is specified by the second 
argument repeats. 

## 4. numpy.random 
# 4.1. numpy.random.randint

The **numpy.random.randint**(low,high=None,size=None,dtype='l') function returns random integers from the interval(low,high). If high parameter 
is missing(None), the random numbers are selected from the interval (0,low). By default, a single random number(int) is returned. To generate 
a narray of random integers, the shape of the array is provided in the parameter size.

This function can be used to simulate random events such as tossing a coin, or rolling a dice as shown below. 

# 4.2. numpy.random.choice 
The **numpy.random.choice**(x,size=None,replace=True,p=None) returns a random sample from a given array. By default, a single value is returned.
To return more elements, the output shape can be specified in the parameter size as we did before with the numpy.random.randint function. 
By default, elements have equal probability of being selected. To assign different probabilities to each element, an array of probabilities
p can be provided.

# 4.3. numpy.random.binomial

We can simulate a wide variety of statistical distributions by using numpy such as normal, beta, binomial, uniform, gamma, or poisson distributions. 

The **numpy.random.binomial**(n,p,size=None) draws samples from a binomial distribution. The binomial distribution is used when there are
two mutually exclusive outcomes, providing the number of successes of n trials with a probability of success on a single trial p. 

## 5.numpy.polyfit 

The **numpy.polyfit**(x,y,deg,rcond=None,full=False,w=None,cov=False) function outputs a polynomial of degree deg that fits the points(x,y), 
minimizing the square error. 

This function can be very useful in linear regression problems. Linear regression models the relationship between a dependent variable
and an independent variable, obtaining a line that best fits the data; $ y=a+bx $ where x  is the independent variable, y is the dependent variable, 
b is the slope, and a is the intercept. To obtain both coefficients a and b. 

##8.numpy.argmax 

The **numpy.argmax**(x, axis=None, out=None) function returns the indices of the maximum values along an axis. 
In a second array, we can easily obtain the index of the maximum value. We can obtain the indeces of maximum values along a specified axis,
providing 0 or 1 to the axis attribute. 


## References: https://en.m.wikipedia.org/wiki/NumPy 
