
import scipy.stats
def sigmoidWrapper(z):
    return scipy.stats.logistic.cdf(z)


import math
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

import timeit
def timingWrapper(n):
    """Time the sigmoidWrapper function using timeit.
Use the function call 'sigmoidWrapper (-10)'.
Test data is not provided, since this will depend on your machine
and will vary subtly each time you run it.
Documentation: https://docs.python.org/3/library/timeit.html
Params: n (int): # of executions of the function
Returns: (float) #seconds required to execute the function n times
"""
    t = timeit.timeit('sigmoidWrapper (-10)', number=n, globals=globals())
    return t

def timingSigmoid(z):
    import timeit
    t=timeit.timeit('sigmoid(-10)', number=z, globals=globals())
    return t