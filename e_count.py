# HW1 problem

def eWrapper (s):
    
    """Count the e's in a string, using the string method 'count'.

    >>> eWrapper ('Every e, please.')
    5
    >>> eWrapper ('Shall I compare thee to a summer's day?')
    4
    >>> eWrapper ('efgEFG efgEFG')
    4

    Params: s (str)
    Returns: (int) #e in s, either lowercase or uppercase
    """

    return s.lower().count('e')

def eCount (s):

    """Count the e's in a string, using for loop and NOT using string.count.

    >>> eCount ('Every e, please.')
    5
    >>> eCount ('Shall I compare thee to a summers day?')
    4
    >>> eCount ('efgEFG efgEFG')
    4

    Params: s (str)
    Returns: (int) #e in s, either lowercase or uppercase
    """
    e = 0
    s = s.lower()
    for i in s:
        if i == 'e':
            e += 1
    return e

def timingWrapper (n):

    """Time the eWrapper function using timeit.

    Use the function call 'eWrapper ("efgEFG")'.  Be careful with the quotes.
    Test data is not provided, since this will depend on your machine
    and will vary subtly each time you run it.

    Documentation: https://docs.python.org/3/library/timeit.html
    Params: n (int): # of executions of the function
    Returns: (float) #seconds required to execute the function n times
    """
    import timeit
    t =timeit.timeit('eWrapper ("efgEFG")', number=n, globals=globals())
    return t

def timingECount (n):

    """Time the eCount function using timeit.

    Use the function call 'eCount ("efgEFG")'.  Be careful with the quotes.
    Test data is not provided, since this will depend on your machine
    and will vary subtly each time you run it.

    Documentation: https://docs.python.org/3/library/timeit.html
    Params: n (int): # of executions of the function
    Returns: (float) #seconds required to execute the function n times
    """
    import timeit
    t = timeit.timeit('eCount ("efgEFG")', number=n, globals=globals())
    return t