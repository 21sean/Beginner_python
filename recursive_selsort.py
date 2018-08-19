# recursion exercises

# ------------------------------------------------------------------------------

def iterative_min (L):
    
    """Minimum element, using a for loop.

    Params:  L (list) elements should be comparable by < (e.g., ints)
    Returns: (int) minimum element of L
    """

    imin = L[0]
    for i in L:
        if imin > i:
            imin = i
    return imin

def iterative_argmin (L):
    
    """Index of minimum element, using a for loop.

    Params:  L (list) elements should be comparable by < (e.g., ints)
    Returns: (int) index of min
    """
    imax = 0
    for i in range(1, len(L)):
        if L[i] < L[imax]:
            imax = i
    return imax


def iterative_argmax (L):
    
    """Index of maximum element, using a for loop.

    Params:  L (list) elements should be comparable by < (e.g., ints)
    Returns: (int) index of max
    """

    imax = 0
    for i in range(1, len(L)):
        if L[i] > L[imax]:
            imax = i
    return imax

def recursive_argmax (L):
    
    """Index of maximum element, recursively.

    Params:  L (list) elements should be comparable by < (e.g., ints)
    Returns: (int) index of max
    """
    if len(L) == 1:
        return L[0]
    else:
        indexMax = iterative_argmax(L)
        clonedL = L[:]
        clonedL[indexMax], clonedL[len(L) - 1] = clonedL[len(L) - 1], clonedL[indexMax]
        tempList = recursive_argmax(clonedL[:len(clonedL) - 1])
        return tempList


# testing (PLEASE DO NOT CHANGE)
A = [10, 7, 8, 9, 2, 5]
print ('A:', A)
mymin = iterative_min(A)    # don't use a variable 'min', clobbering builtin min
if mymin != None:
    print ('min element of A is ', mymin)
imin = iterative_argmin(A)
if imin != None:
    print ('min element of A is ', A[imin])
imax = iterative_argmax(A)
if imax != None:
    print ('max element of A is ', A[imax])
imax = recursive_argmax(A)
if imax != None:
    print ('max element of A is ', A[imax])

# ------------------------------------------------------------------------------

def recursive_selSort (L):

    """Selection sort, recursive argmax version.

    This solution is suboptimal for efficiency, 
    because of all the cloned lists you have to create 
    (which require expensive copying).
    So in practice you would not use recursion for selection sort.
    But it is a good intellectual exercise to better understand recursion.

    Algorithm:
    - base case: if L is length 0 or 1, solve directly

    [do a small amount of work]
    - compute maximum of entire list
    - clone the list (before you change it, to avoid changing it outside)
    - in this cloned list, swap max to the last position
    - store this max elt (so that you can append it after the recursive call)

    - recursively sort a prefix of the list, by slicing out the last element
      (note that this is a smaller list since it doesn't include last element)

    [mop up]
    - append the original maximum element to the recursively sorted list
    - return this list, which is the entire sorted list
    Params: L (list, int or float): 
    Returns: (list, same type as L) new sorted list
    """
    if len(L) == 1:
        return L
    else:
        indexMax = iterative_argmax(L)
        clonedL = L[:]
        clonedL[indexMax], clonedL[len(L) - 1] = clonedL[len(L) - 1], clonedL[indexMax]
        tempList = recursive_selSort(clonedL[:len(clonedL) - 1])
        tempList.append(clonedL[len(clonedL) - 1])
        return tempList
# ------------------------------------------------------------------------------
# PLEASE DO NOT CHANGE CODE BELOW THIS LINE

# testing 
A_sorted = recursive_selSort (A)
print ("Sorted list: " + str(A_sorted))

from random import *
def genInts (n, lo, hi):

    """Generate a random list of integers.
    Params: 
        n (int) #integers
        lo, hi (int): choose ints in the interval [lo, hi], lo < hi
    Returns: (int list)
    """

    assert lo < hi
    L = []
    for i in range(n):
        L.append(randrange(lo, hi+1))
    return L

A = genInts (10, 0, 999)
print ("Original list: " + str(A))
A_sorted = recursive_selSort (A)
print ("Sorted list:   " + str(A_sorted))
