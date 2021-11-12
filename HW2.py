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

# *Correction*
#
# Docstring: -5
#
# Q1: -2 for not using assert correctly

# ## Problem Set 2
# **Stats 507, Fall 2021**
#
# *Sachie Kakehi*
#
# *October 1, 2021*
#
# Contents
# + [Question 0](#Question-0)
# + [Question 1](#Question-1)
# + [Question 2](#Question-2)

# ## Question 0 - Code review warmup [10 points]
#
# Code snippet

sample_list = [(1, 3, 5), (0, 1, 2), (1, 9, 8)]
op = []
for m in range(len(sample_list)): 
    li = [sample_list[m]]
    for n in range(len(sample_list)):
            print(len(sample_list))
            if (sample_list[m][0] == sample_list[n][0] and sample_list[m][2] != sample_list[n][2]):
                li.append(sample_list[n])
                print('append li', li)
    op.append(sorted(li, key=lambda dd: dd[2], reverse=True)[0])
    print('op', op)
res = list(set(op))
print('res', res)

# **Instructions**
#
# **Concisely describe what task the code above accomplishes. Say what it does (in total) and not how it accomplishes it. You may wish to understand the snippet step-by-step, but your description should not state each step individually.**
#
# -------------------------------------------------------------------------
#
# The code above does not work. To fix the code, the 3 should be a 2 since the list starts from 0, not 1.
# Additionally in terms of structure the second for loop does not need to be indented.
# The code iterates through each row of the sample list and eliminates tupules with the same first position number but have a smaller third position number.
#
#
#
# -------------------------------------------------------------------------
# **Write a short code review that offers 3-5 (no more) concrete suggestions to make the snippent more efficient, literate (easier to read), or “pythonic”.
# Focus your suggestions on concepts or principles that would help the author of this code snippet write better code in the future.**
#
# -------------------------------------------------------------------------
#
# 1. As mentioned above, to ensure the code works, the 3 should be a 2.
# 2. The code can be made more efficient by eliminating a list having a set. We are only getting one tupule from the whole list so we don't need sorted because we will no longer hold a list inside of the for loop. Instead we can use a tupule to hold the largest third key with the same first key.
# 3. Instead of using a list we can initialize a set to get rid of the duplicates. In our initial code op is a list that holds three values and can hold duplicates, which we don't want.
#

# ## Question 1 - List of Tuples
# Write a function that uses NumPy and a list comprehension to generate # a random list of n k-tuples containing integers ranging from low to high.
# Choose an appropriate name for your function, and reasonable default values for # k, low, and high.
# Use assert to test that your function returns a list of tuples.

import numpy as np
import pandas as pd
from timeit import Timer
from collections import defaultdict

# +
rng = np.random.default_rng()

def Tuple(n, k, low, high):
    """
    Generate a random list of n k-tuples of length tup_size of integers low to high.

    Parameters
    ----------
    n : integer
        The number of tuples in the list.
    k : integer
        The length of the tuples created.
    low : integer
        The low end of the range to generate integers from.
    high : integer
        The high end of hte range to generate integers from.
    
    Returns
    -------
    A list of length `n` with tuples of size `k` consisting of uniform
    random integers in from low to high.
    """
    res = list()
    for i in range(n):
        rints = rng.integers(low=low, high=high, size=k)
        res.append(tuple(rints))
    return(res)
    assert type(tuple(res)) is tuple


# -

assert len(Tuple(10,3,0,1000)) == 10
assert all([isinstance(x, tuple) for x in Tuple(5,3,0,1000)])


# ## Question 2 - Refractor the Snippet
# In this question, you will write functions to accomplish the goal you concisely described in part “a” of the warm up.
#
# a) Encapsulate the code snippet from the warmup into a function that parameterizes the role of 0 and 3 and is otherwise unchanged. Choose appropriate names for these paramters.

def Snip(key, value, n, k, low, high):
    """    
    Find tuples with maximum value in one position `key` by common value in another `value`.
    
    Among all tuples in list sharing a common value in the `value`position,
    find those also having maximum value in the `key` position. 

    Parameters
    ----------
    key : integer
        The position within the tuples to maximize.
    value : integer
        The position within the tuples to compare.
    n : integer
        The number of tuples in the list.
    k : integer, optional
        The length of the tuples created.
    low : integer, optional
        The low end of the range to generate integers from.
    high : integer, optional
        The high end of hte range to generate integers from.

    Returns
    -------
    A list of all tuples, where, for each unique `value` position, the maximum
    value in the `key` position is achieved.    

    """
    sample_list = Tuple(n, k, low, high)
    op = []
    for m in range(len(sample_list)): 
        li = [sample_list[m]]
        for n in range(len(sample_list)):
                if (sample_list[m][key] == sample_list[n][key] and sample_list[m][value] != sample_list[n][value]):
                    li.append(sample_list[n])
        op.append(sorted(li, key=lambda dd: dd[2], reverse=True)[0])
    res = list(set(op))
    return res


# b) Write an improved version of the function form part a that implements the suggestions from the code review you wrote in part b of the warmup.

def Improv(key, value, n, k, low, high):
    """    
    Find tuples with maximum value in one position `key` by common value in another `value`.
    
    Among all tuples in list sharing a common value in the `value`position,
    find those also having maximum value in the `key` position. 

    Parameters
    ----------
    key : integer
        The position within the tuples to maximize.
    value : integer
        The position within the tuples to compare.
    n : integer
        The number of tuples in the list.
    k : integer, optional
        The length of the tuples created.
    low : integer, optional
        The low end of the range to generate integers from.
    high : integer, optional
        The high end of hte range to generate integers from.

    Returns
    -------
    A list of all tuples, where, for each unique `value` position, the maximum
    value in the `key` position is achieved.     
    
    """
    sample_list = Tuple(n, k, low, high)
    res = set()
    for m in range(len(sample_list)):
        largest = sample_list[m]
        for n in range(len(sample_list)):
            if (sample_list[m][key] == sample_list[n][key] and largest[value] < sample_list[n][value]):
                largest = sample_list[n]
        res.add(largest)
    return(list(res))


# c) Write a function from scratch to accomplish the same task as the previous two parts.
# Your solution should traverse the input list of tuples no more than twice.
# Hint: consider using a dictionary or a default dictionary in your solution.

def Scratch(key, value, n, k, low, high):
    """    
    Find tuples with maximum value in one position `key` by common value in another `value`.
    
    Among all tuples in list sharing a common value in the `value`position,
    find those also having maximum value in the `key` position. 

    Parameters
    ----------
    key : integer
        The position within the tuples to maximize.
    value : integer
        The position within the tuples to compare.
    n : integer
        The number of tuples in the list.
    k : integer, optional
        The length of the tuples created.
    low : integer, optional
        The low end of the range to generate integers from.
    high : integer, optional
        The high end of hte range to generate integers from.

    Returns
    -------
    A list of all tuples, where, for each unique `value` position, the maximum
    value in the `key` position is achieved.     
    
    """
    sample_list = Tuple(n, k, low, high)
    res = dict()
    for sample in sample_list:
        if sample[key] not in res.keys() or sample[value] > res.get(sample[key])[value]:
            res.update({sample[key]: sample})
    return(list(res.values()))


# d) Use the function you wrote in question 1 to generate a list of tuples as input(s), run and summarize a small Monte Carlo study comparing the execution times of the three functions above (a-c).

# +
n_mc = 30 # take sample of 30
res = defaultdict(list)
  
for i in range(n_mc):
    n = rng.integers(1, high=100)
    k = rng.integers(2, high=100)
    high = rng.integers(1, high=100)
    low = rng.integers(0, high=high)
    key = rng.integers(0, high=k)
    value = rng.integers(0, high=k)
    res["n"].append(n)
    res["k"].append(k)
    res["high"].append(high)
    res["low"].append(low)
    res["key"].append(key)
    res["value"].append(value)
    for f in (Snip, Improv, Scratch):
        # generate parameters
        # calc time
        t = Timer("f(key, value, n, k, low, high)", globals={"f": f, "key": key, "value": value, "n": n, "k": k, "low": low, "high": high})
#        m1 = np.median([t.timeit(1) for i in range(n_mc)]) 
        m2 = np.mean([t.timeit(1) for i in range(n_mc)])            
        res[f.__name__].append(round(m2 * 1e6, 1))
        

# construct a table

res = pd.DataFrame(res)
t1 = res.to_html(index=False)
t1 = t1.rsplit('\n')
tab1 = ''
for i, line in enumerate(t1):
    tab1 += line
    if i < (len(t1) - 1):
        tab1 += '\n'
# -




