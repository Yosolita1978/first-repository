def remove(words, to_remove):
    """ 
    Given a list it will return the list without the word to remove

    >>> remove(['foo', 'bar', 'baz'], 'bar')
    ['foo', 'baz']

    >>> remove(['foo', 'bar', 'baz', 'bar'], 'bar')
    ['foo', 'baz']

    """

    if len(words) == 0:
        return words

    rest = remove(words[1:], to_remove)
    if words[0] == to_remove:
        return rest
    else:
        return words[:1] + rest 


def is_palindrome(word):

    """ 
    >>> is_palindrome("378873")
    True

    >>> is_palindrome("8873")
    False

    >>> is_palindrome("0011")
    False

    >>> is_palindrome("9999")
    True

    >>> is_palindrome("0")
    True

    >>> is_palindrome("")
    True

    """

    if len(word) == 0:
        return True

    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False


def make_palindrome(s, k):
    """ 
    >>> make_palindrome("3943",1)
    '3993'

    >>> make_palindrome("0011",1)
    '-1'

    >>> make_palindrome("378983",2)
    '389983'
    
    >>> make_palindrome("367873",2)
    '378873'
    """

    if k == -1:
        return "-1"

    if len(s) == 0:
        return s

    if s[0] == s[-1]:
        rest = make_palindrome(s[1:-1], k)
        add = s[0]
    else:
        rest = make_palindrome(s[1:-1], k-1)
        if s[0] < s[-1]:
            add = s[-1]
        else:
            add = s[0]

    
    if rest == "-1":
        return "-1"

    return add + rest + add


if __name__ == "__main__":
    import doctest
    doctest.testmod()



