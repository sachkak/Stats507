# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# *Comments:*
#
# Only one file: -10
#
# Docstring: -10
#
# Q0: -1
#
# Q1: -3 for no testing
#
# Q2: -3 for not being staggered

# ## Problem Set 1
# **Stats 507, Fall 2021**  
# *Sachie Kakehi*  
#
#
# ## Contents
# + [Question 0](#Question-0)
# + [Question 1](#Question-1)
# + [Question 2](#Question-2)
# + [Question 3](#Question-3)

# ## Question 0

# '''
# <hr />
#
# This is *question 0* for [problem set 1](https://jbhender.github.io/Stats507/F21/ps/ps1.html) of [Stats 507](https://jbhender.github.io/Stats507/F21/).
#
# <blockquote>Question 0 is about Markdown.</blockquote>
#
# The next question is about the **Fibonnaci sequence**, $Fn = F_{n−2} + F_{n−1}$. In part **a** we will define a Python function <code>fib_rec()</code>.
#
# Below is a …
#
# <h3>Level 3 Header 3</h3>
# Next, we can make a bulleted list:
#
# - Item 1
#     - detail 1
#     - detail 2
# - Item 2
#
# Finally, we can make an enumerated list:
#
# 1. Item 1
# 2. Item 2
# 3. Item 3
#
# <hr />
# '''

# ## Question 1

import statistics
import pandas as pd
from timeit import default_timer as timer
from datetime import timedelta


# Write a recursive function fib_rec() that takes input n, a=0, and b=1 and returns the value of Fn for F_0 = a, and F_1 = b. [You can call a and b something else, e.g. f0 and f1 or collect them in a list/tuple if you prefer.]

def fib_rec(n):
    """
    Compute the Fibonacci number $F_n$, when $F_0 = a$ and $F_1 = b$.
    
    This function computes $F_n$ using a linear-complexity recursion.

    Parameters
    ----------
    n : int
        The desired Fibonacci number $F_n$.

    Returns
    -------
    The Fibonacci number $F_n$.

    """
    if n < 0:
       print("Plese enter a positive integer")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)


#Test to ensure correct 7th, 11th, and 13th Fibonacci numbers are returned.
print(fib_rec(7))
print(fib_rec(11))
print(fib_rec(13))


# Write a function fib_for() with the same signature that computes Fn by summation using a for loop.

def fib_for(n):
    """
    Compute the Fibonacci number $F_n$, when $F_0 = a$ and $F_1 = b$.

    This function computes $F_n$ directly by iterating using a for loop.

    Parameters
    ----------
    n : int
        The desired Fibonacci number $F_n$. 

    Returns
    -------
    The Fibonacci number $F_n$. 

    """
    n1, n2 = 0, 1
    count = 0
    if n < 0:
       print("Plese enter a positive integer")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
       for i in range(n):
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1
       return(n1)


# Write a function fib_whl() with the same signature that computes Fn by summation using a while loop.

def fib_whl(n):
    """
    Compute the Fibonacci number $F_n$, when $F_0 = a$ and $F_1 = b$.

    This function computes $F_n$ by direct summation, iterating using a
    while loop.

    Parameters
    ----------
    n : int
        The desired Fibonacci number $F_n$.

    Returns
    -------
    The Fibonacci number $F_n$.

    """
    n1, n2 = 0, 1
    count = 0
    if n < 0:
       print("Plese enter a positive integer")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
       while count < n:
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1
       return(n1)


# Write a function fib_rnd() with the same signature that computes Fn using the rounding method described on the Wikipedia page linked above.

def fib_rnd(n):
    """
    Directly compute the Fibonacci number $F_n$, when $F_0 = a$ and $F_1 = b$.

    This function computes $F_n$ by rounding $\phi^n / sqrt(5)$.
    The formula is used directly for n < 250, and is applied on the log scale
    for 250 <= n < 1478. A ValueError is raised for larger n to avoid
    overflow errors.


    Parameters
    ----------
    n : int
        The desired Fibonacci number $F_n$, must be less than 1478.
    Returns
    -------
    The Fibonacci number $F_n$ if n < 1478, else a ValueError.
    """
    phi = 0.5*(1+(5 ** 0.5))
    if n < 0:
       print("Plese enter a positive integer")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
       return round((phi ** n) / (5 ** 0.5))


# Write a function fib_flr() with the same signature that computes Fn using the truncation method described on the Wikipedia page linked above.

def fib_flr(n):
    """
    Directly compute the Fibonacci number $F_n$, when $F_0 = a$ and $F_1 = b$.

    This function computes $F_n$ by finding the smallest integer less than
    $\phi^n / sqrt(5) + 0.5$. The formula is used directly for n < 250, and is
    applied on the log scale for 250 <= n < 1477. A ValueError is raised for
    larger n to avoid integer overflow.


    Parameters
    ----------
    n : int
        The desired Fibonacci number $F_n$, must be less than 1478.

    Returns
    -------
    The Fibonacci number $F_n$ if n < 1477, else a ValueError.
    """
    phi = 0.5*(1+(5 ** 0.5))
    if n < 0:
       print("Plese enter a positive integer")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
       return round((phi ** n) / (5 ** 0.5)+0.5)


# For a sequence of increasingly large values of n compare the median computation time of each of the functions above. Present your results in a nicely formatted table. (Point estimates are sufficient).

functions = [fib_rec, fib_for, fib_whl, fib_rnd, fib_flr]  # list of functions
ntest = [5, 10, 15, 20, 25, 30, 35, 40]
df = pd.DataFrame(ntest)
for fn in functions:
    data = []       
    for i in 5, 10, 15, 20, 25, 30, 35, 40:
        med = []
        for j in range(1, 6):
            start = timer()
            fn(i)
            elapsed_rec = timedelta(seconds=timer()-start)
            med.append(elapsed_rec)
        data.append(statistics.median(med))
    df['{}'.format(fn)] = pd.DataFrame(data)
print(df)


# ## Question 2 - Pascal’s Triangle [20]
# Pascal’s triangle is a way to organize, compute, and present the Binomial coefficients (nk). The triangle can be constructed from the top starting with rows 0 [(00)=1], and 1 [(10)=1, (11)=1]. From there, subsequent rows can be computed by adding adjacent entries from the previous row (implicitly appending zeros on the left and right).
# Write a function to compute a specified row of Pascal’s triangle. An arbitrary row of Pascal’s triangle can be computed efficiently by starting with (n0)=1 and then applying the following recurrence relation among binomial coefficients,
# (nk)=(nk−1)×n+1−kk.

# +
def PascalRow(n):
    """
    Compute an arbitrary row of Pacal's triangle.

    Row 0 is "1", row 1 is "1, 1".  

    Parameters
    ----------
    n : int
        The desired row.
 
    Returns
    -------
    A list with values for the desired row. 
    """
    C = 1
    for j in range(1, n+1):
        print(' ', C, sep='', end='')
        C = C * (n - j) // j
    return
        
        
print(PascalRow(3))


# -

# Write a function for printing the first n rows of Pascal’s triangle using the conventional spacing with the numbers in each row staggered relative to adjacent rows. Use your function to display a minimum of 10 rows in your notebook.

def Pascal(n):
    """
    Compute an arbitrary row of Pacal's triangle.

    Row 0 is "1", row 1 is "1, 1".  

    Parameters
    ----------
    n : int
        The desired number of rows. 
 
    Returns
    -------
    A string which, when printed, displays the first n rows. 
    """
    for i in range(1, n+1):
        #stagger
        for j in range(0, n-i+1):
            print(' ', end='')
        C = 1
        for j in range(1, i+1):
            #print first row
            print(' ', C, sep='', end='')
            #print next rows
            C = C * (i - j) // j
        print()


# ## Question 3

import numpy as np
import scipy.stats as st
import pandas as pd


# ### Part A
# Normal

def normal(data, level, ci_format):
    data = 1.0 * np.array(data)
    n = len(data)
    est, se = np.mean(data), st.sem(data)
    h = se * st.t.ppf((1 + level) / 2., n-1)
    low = est - h
    up = est + h
    if ci_format == True:
        return('{}'.format(est) + '['+'{}'.format(level*100) + '%CI :' + '(' + '{0}: {1}'.format(low, up) + ')]')
    else:
        res2 = dict(est = est, lwr=low, upr=up, level=level)
        return(res2)


# ### Part B
# Write a function to return point and interval estimates based on several of these methods.
# Your function should have a parameter method that controls the method used

def CI(data, level, method, ci_format):
    """
    Construct point and interval estimates for a population proportion.

    The "method" argument controls the estimates returned. Available methods
    are "Normal", to use the normal approximation to the Binomial, "CP" to
    use the Clopper-Pearson method, "Jeffrey" to use Jeffery's method, and
    "AC" for the Agresti-Coull method.

    By default, the function returns a string with a 95% confidence interval
    in the form "mean [level% CI: (lwr, upr)]". Set `str_fmt=None` to return
    a dictionary containing the mean, confidence level (%-scale, level),
    lower bound (lwr), and upper bound (upr) can also be returned.

    Parameters
    ----------
    data : A 1-dimensional NumPy array or compatible sequence type (list, tuple).
        A data vector of 0/1 or False/True from which to form the estimates.
    level : float, optional.
        The desired confidence level, converted to a percent in the output.
        The default is 0.95.
    method: str, optional
        The type of confidence interval and point estimate desired.  Allowed
        values are "bionmial" for the normal approximation to the Binomial,
        "ClopperPearson" for a Clopper-Pearson interval, "Jeffrey" for Jeffrey's method,
        or "AgrestiCoull" for the Agresti-Coull estimates.
    ci_format: bool.
        If `True` a string with a (100 * level)% confidence interval in the form
        "mean [(100 * level)% CI: (lwr, upr)]" is returned.
        Else a dictionary containing the keywords in the string is returned.

    Returns
    -------
    A string with a (100 * level)% confidence interval in the form
    "mean [(100 * level)% CI: (lwr, upr)]" or a dictionary containing the
    keywords shown in the string.

    """
    if isinstance(data, (list, tuple, np.ndarray)) == True:
        data = 1.0 * np.array(data)
        if method == 'binomial':
            # Part B_i - Normal approximation to the Binomial distribution
            #def binomial(data, level, ci_format):
                # sample prop = X/N
                x = np.count_nonzero(data == 1)
                n= len(data)
                est = x/n
                # p ± z * sqrt(p*(1−p)/n)
                p = est
                z = st.norm.ppf(level)
                low = est - z * ((p*(1-p))/n ** 0.5)
                up = est + z * ((p*(1-p))/n ** 0.5)
                # np^∧n(1−p^)>12 should yield warning
                if (n*p or n*(1-p) > 12):
                    if (ci_format == True):
                        return('{}'.format(est) + '['+'{}'.format(level*100) + '%CI :' + '(' + '{0}: {1}'.format(low, up) + ')]')
                    else:
                        #res1 = {"est", "lwr", "upr", "level"}
                        res2 = dict(est = est, lwr=low, upr=up, level=level)
                        return(res2)
                        #return(dict(est = est, low, up, level))
                        # res1 == res2 # same keys and values
                        # return(res2)
                else:
                    print("WARNING!  np∧n(1−p)>12")    
        if method == "ClopperPearson":
            # Part B_ii
            #The Clopper-Pearson interval for a population proportion can be expressed using quantiles from Beta distributions.
            #Specifically, for a sample of  the interval is,
            #(θ^L,θ^U)=(B(α2,x,n−x+1),B(1−α2,x+1,n−x)).
            # def ClopperPearson(data, level, ci_format):
                # size n with x successes and α 1 minus the confidence level
                n= len(data)
                x = np.count_nonzero(data == 1)
                p = x/n
                est = p
                alpha = 1- level
                if x==0:
                    low = 0
                else:
                    low = st.beta.interval(alpha, x,n-x+1)[0]
                if x==n:
                    up =1
                else:
                    up = st.beta.interval(1-alpha, x+1,n-x)[1]
                if (ci_format == True):
                    return('{}'.format(est) + '['+'{}'.format(level*100) + '%CI :' + '(' + '{0}: {1}'.format(low, up) + ')]')
                else:
                    res2 = dict(est = est, lwr=low, upr=up, level=level)
                    return(res2)
        if method == "Jeffrey":
            # Part B_iii
            # Jeffrey’s interval is a Bayesian credible interval with good frequentist properties.
            # It is similar to the Clopper-Pearson interval in that it utilizes Beta quantiles,
            # but is based on a so-called Jeffrey’s prior of B(p,0.5,0.5).
            # Specifically, the Jeffrey’s interval is
            # (0∨B(α/2,x+0.5,n−x+0.5),B(1−α/2,x+0.5,n−x+0.5)∧1). (Use the sample proportion as the point estimate).
            # def Jeffrey(data, level, ci_format):
                # sample prop = X/N
                n= len(data)
                x = np.count_nonzero(data == 1)
                p = x/n
                est = p
                alpha = 1- level
                if x==0:
                    low = 0
                else:
                    low = st.beta.interval(alpha/2, x+0.5,n-x+0.5)[0]
                if x==n:
                    up =1
                else:
                    up = st.beta.interval(1-alpha/2, x+1,n-x)[1]
                if (ci_format == True):
                    return('{}'.format(est) + '['+'{}'.format(level*100) + '%CI :' + '(' + '{0}: {1}'.format(low, up) + ')]')
                else:
                    res2 = dict(est = est, lwr=low, upr=up, level=level)
                    return(res2)
        if method == "AgrestiCoull":
            # Part B_iiIi
            # Agresti-Coull interval arises from a notion “add 2 failures and 2 successes” as a means of regularization.
            # More specifically, define n~=n+z^2 and p~=(x+z^2/2)/n~.
            # The Agresti-Coull interval is Normal approximation interval using p~ in place of p^.
            # def AgrestiCoull(data, level, ci_format):
                # sample prop = X/N
                z = st.norm.ppf(level)
                n = len(data) + z**2
                x = np.count_nonzero(data == 1)
                p = (x+(z**2)/2)/n
                est = p
                alpha = 1- level
                low = est - z*((p*(1-p))/n ** 0.5)
                up = est + z*((p*(1-p))/n ** 0.5)
                if (ci_format == True):
                    return('{}'.format(est) + '['+'{}'.format(level*100) + '%CI :' + '(' + '{0}: {1}'.format(low, up) + ')]')
                else:
                    res2 = dict(est = est, lwr=low, upr=up, level=level)
                    return(res2)
        else:
            print("check for correct method")
    else:
        print("data not array")


# ### Part C
# Create a 1d Numpy array with 42 ones and 48 zeros.

arr = np.concatenate((np.zeros(48), np.ones(10)))
ci_format = False
# Construct a nicely formatted table comparing 90, 95, and 99% confidence intervals using each of the methods above (including part a) on this data.
output = []       
for level in 0.9, 0.95, 0.99:
    output.append(normal(arr, level, ci_format))
    fn = CI
    for method in ["binomial", "ClopperPearson", "Jeffrey", "AgrestiCoull"]:
        output.append(fn(arr, level, method, ci_format))
df = pd.DataFrame.from_dict(output)
df.index = ["normal", "binomial", "ClopperPearson", "Jeffrey", "AgrestiCoull"]*3
df['delta_interval'] = df['upr']-df['lwr']
print(df)

# QUESTION: For each confidence level, which method produces the interval with the smallest width?
#
#
# The binomial distribution has the lowest delta_interval.


