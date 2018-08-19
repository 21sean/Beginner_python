
from random import *

def randomSubset (B):
    """Build a random subset A of B, using lists to simulate sets.
    Algorithm:
    - build an empty list A to get started
    - choose the size n of the subset A randomly (no bigger than the set!)
      thought exercise: how do you find the size of a set(list) B? len(B)
    - repeatedly choose an element x at random from the set B;
      if it is already in the subset, throw it away (a set has no duplicates)

   # >>> randomSubset ([1, 2, 3, 4])
    [4,2]
    #>>> randomSubset ([10, [2], [[3, 10]])
    [ [[3, 10] ]
    #>>> randomSubset ([10, [2], [[3, 10]])
    []

    Params: B (list): a set, represented internally as a list
    Returns: (list) a randomly chosen subset of B, represented as a list
    """
    A = []
    n = randrange(1, len(B) + 1)
    for i in range(0, n):
        x = choice(B)
        if x not in A:
            A.append(x)
    return A

# testing this function
B = [1,2,3,4]
A = randomSubset (B)
print (A)


B = [[1], [[[2], []], [5]]]
A = randomSubset (B)
print (A)

# ------------------------------------------------------------------------------

def isSubset (A, B):

    """Is A a subset of B?
    A is a subset of B if every element of A is an element of B.
    
    In this version, you will get a better understanding of the subset
    relationship by using a nested for loop (for loop inside a for loop)
    instead of letting 'in' do all the heavy lifting.

    old version (in subset.py):
    for each element a of A
        is a in B?

    becomes

    new version:
    for each element a of A
        for each element b of B
            is a == b?
        if any b answered yes, a passes the test
        otherwise a fails, so a is not in B, so A is not a subset of B
    if you haven't failed yet, everyone must have passed: success!
    Params:
        A (list): a set of *integers*, represented internally as a list
        B (list): another set of integers, represented internally as a list
    Returns: (bool) is A a subset of B?
    """

    for a in A:
        test = False
        for b in B:
            if b == a:
                test = True
        if not test:
            return False
    return True


B = [1,2,3,4]
A = randomSubset (B)
answer = isSubset (A, B)
print (answer) # hopefully True
