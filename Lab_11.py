from math import sqrt
from random import *
L = [1, 2, 3, 4, 5, 6]


def computeAvg(list):
    """ compute the average of jan birthdays from 1200 random ints in
        the range 1,365.
     #   >>> compute_avg_jan_bd (birthdays.dat)
        107.6
        Params: a (list)
        Returns: (float) average the number of jan. dates i.e. dates
    less than 32.
    """
    n = sum(list)
    m = len(list)
    return n/m


def variance(a):
    var = []
    for i in a:
        var.append((i - computeAvg(a)) ** 2)
    return computeAvg(var)


def standardDeviation (a):
    return sqrt(variance(a))


print("The average of my list is:", computeAvg(L))
print("The variance of my list is:",  variance(L))
print("The Standard Deviation of my list is:", standardDeviation(L))


#--------------------------------------------------------------------------------------
def coinExperiment (a):
    """Simulate an experiment of n coin flips.
        Params:
        n (int): # coin flips
        p (float): probability of heads
        Returns: (int) # heads
        """
    nh = 0
    for i in range(100):
        nh += random() < a
    return nh
def repeatExperiment(a):
    heads = []
    for i in range(1000):
        heads.append(coinExperiment(a))
    return heads
def computeavgFlip(a):
    heads = []
    for i in range(1000):
        heads.append(coinExperiment(a))
    return computeAvg(heads)
def varianceCoin(a):
    """var = 0
    Avg = computeavgFlip(a)
    for i in a:
        var += (Avg - i) ** 2
    return var / len(a)"""
    heads=[]
    for i in range(1000):
        heads.append(coinExperiment(a))
    return variance(heads)
def standardeviationCoin (a):
    """compute the standard deviation from a number of coin tosses by taking sqrt of variance.
     #  >>> compute_avg_jan_bd (birthdays.dat)
        107.6
        Returns: (float) standard deviation
        """
    return standardDeviation(repeatExperiment(a))

#rigged = repeatExperiment(coinExperiment (100, p=.7))#probability is tilted

print("----------------------------------------------------------------------------------------")
print("For this trial: 1000 simulations, and 100 coin flips per sim.")
print("The coin had a weight of 0.5")
print("The average result from the trials was:", computeavgFlip(.5))
print("The variance was:", varianceCoin(.5))
print("The Standard Deviation of your trial is:", standardeviationCoin(.5))
print("----------------------------------------------------------------------------------------")
print("For this trial: 1000 simulations, and 100 coin flips per sim.")
print("The coin had a weight of 0.7 ~ Rigged")
print("The average result from the trials was:", computeavgFlip(.7))
print("The variance was:", varianceCoin(.7))
print("The Standard Deviation of your trial is:", standardeviationCoin(.7))
