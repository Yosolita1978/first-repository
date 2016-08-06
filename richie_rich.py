
def make_palindrome(s, k):
    """
    Returns a palyndrome version of S.

    If more than k edits are needed, returns -1.

    >>> make_palindrome("3943",1)
    '3993'

    >>> make_palindrome("092282",3)
    '292292'

    >>> make_palindrome("3973",2)
    '3993'

    >>> make_palindrome("3793",2)
    '3993'

    >>> make_palindrome("0011",1)
    -1

    >>> make_palindrome("378983",2)
    '389983'

    >>> make_palindrome("367873",2)
    '378873'

    """
    new_word = ""
    x = 0
    y = len(s)-1
    count = 0

    while x < y:
        if s[x] < s[y]:
            new_word = new_word + s[y]
            count = count +1
        elif s[x] > s[y]:
            new_word = new_word + s[x]
            count = count + 1
        else:
            new_word = new_word + s[x]            

        x = x + 1
        y = y - 1

    if count > k:
        return -1
    
    return new_word + "".join(reversed(new_word))

if __name__ == "__main__":
    import doctest
    doctest.testmod()


