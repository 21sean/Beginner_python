
# recursion exercises (two classics)

def reverseR(s):
    """Reverse a string recursively.

    Hint: there are two base cases and one recursive call.

    >>> reverseR ('dessert')
    tressed

    Params: s (str)
    Returns: reversal of s
    """
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s
    else:
        return reverseR(s[1:]) + s[0]


# testing this function (PLEASE DO NOT CHANGE)
s = ''  # always test extreme cases
print(reverseR(s))
s = 'a'  # what do you always test?
print(reverseR(s))
s = 'dessert'  # a reverse-pair or emiordnilap)
print(reverseR(s))
s = 'drawer'  # another
print(reverseR(s))
s = 'lager'  # yet another
print(reverseR(s))
s = 'golf'  # and one more for good luck
print(reverseR(s))


# ------------------------------------------------------------------------------

def factorialR(n):
    """Factorial, recursively.

    >>> factorialR (4)
    24

    Params: n (int) n>=1
    Returns: n!
    """

    if n < 1:
        return 1
    if n >= 1:
        return factorialR(n-1) * n


# testing this function (PLEASE DO NOT CHANGE)
n = 1  # what do you always test?
print(str(n) + '! = ' + str(factorialR(n)))
n = 3  # continue with something else you know
print(str(n) + '! = ' + str(factorialR(n)))
n = 4  # and more you know
print(str(n) + '! = ' + str(factorialR(n)))
n = 10  # maybe you can even compute this to doublecheck accuracy
print(str(n) + '! = ' + str(factorialR(n)))
n = 100  # then throw caution to the wind; yikes, that is big
print(str(n) + '! = ' + str(factorialR(n)))
