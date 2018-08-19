def hurray (n):
    """Count from 0 to n, inclusive, marking the powers of 2 with 'hurray'.

    As you pass a number that is not a power of 2, print it.
    As you pass a power of 2, instead print 'hurray'.
    To simplify, you will not add any white space to the string.
    
    >>> hurray (1)
    0hurray

    >>> hurray (2)
    0hurrayhurray

    >>> hurray (7)
    0hurrayhurray3hurray567

    Params: n (int) n>=0
    Returns: (str) the integers 0 through n (inclusive)
                   with 'hurray' replacing each power of 2
    """
    hurray = ""
    for i in range(n + 1):
        if ((i != 0) and not (i & (i - 1))):
            hurray += "hurray"
        else:
            hurray += str(i)
    return(hurray)
