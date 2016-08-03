# def is_paly(string):
#     return string[:len(string)//2] == "".join(reversed(string[len(string) - len(string)//2:]))

# print is_paly("hello")
# print is_paly("noon")
# print is_paly("3993")
# print is_paly("992299")

def palyndrome(s, k):
    """
    Returns a palyndrome version of S.

    If more than k edits are needed, returns -1.

    >>> palyndrome("3993",0)
    '3993'

    >>> palyndrome("43993",1)
    -1

    >>> palyndrome("3973",2)
    '3993'

    >>> palyndrome("3793",2)
    '3993'

    """
    x = 0
    y = len(s)-1
    count = 0
    new_word = ""
    while x < y:
        new_word = new_word + s[x]
        if s[x] != s[y]:
            count = count + 1
        x = x + 1
        y = y - 1

    if count > k:
        return -1
    
    return new_word + "".join(reversed(new_word))

if __name__ == "__main__":
    import doctest
    doctest.testmod()


# palyndrome("3993",0)
# assert palyndrome("43993",4) == 2
# assert palyndrome("3793",4) == 1
# assert palyndrome("0",4) == 0
# assert palyndrome("",4) == 0
