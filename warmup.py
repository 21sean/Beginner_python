

def sayBye (s):
    
    """How to say goodbye in a few languages.

    >>> sayBye ('English')
    Goodbye!
    >>> sayBye ('French')
    Au revoir!
    >>> sayBye ('Italian')
    Ciao!

    Params: s (str): a language (only 3 choices: 'English', 'French', 'Italian')
    Returns: (str) how to say goodbye to a person in this language
    """

    if s == 'English':
        return 'Goodbye!'
    elif s == 'French':
        return 'Au revoir!'
    elif s == 'Italian':
        return 'Ciao!'

def sumSquares (n):

    """Compute 1+4+...+n^2, the sum of the first n squares.

    >>> sumSquares (2)
    5
    >>> sumSquares (10)
    385

    Params: n (int) n >= 1
    Returns: (int) 1 + 4 + 9 + ... + n^2 (that is, \sum_{i=1}^n i^2)
    """

    ss = 0
    for i in range(1, n+1):
        ss += i ** 2
    return ss

def upToFirstE (s):

    """Prefix up to first 'e'.

    >>> upToFirstE ("I'll be darned.")
    I'll be darn
    >>> upToFirstE ("Wow, this string has zippo."
    Wow, this string has zippo.
    >>> upToFirstE ("prefix")
    pr
    
    Params: s (str) 
    Returns: (str) prefix of s up to but not including first 'e';
                   if there is no 'e', return the entire string
    """
    c=''
    for i in s:
      if i!= 'e':
          c += i
      else:
          break
    return (c)