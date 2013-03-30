import sys
print( __name__)

def is_palindrome(s):
    """ (str) -> bool
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    """
    return s==reverse(s)


def reverse(s):
    """ (str) -> str
    returns a reveresed copy of s
    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """
    rev=''
    for letter in s:
        rev=letter+rev
        
    return rev


if __name__=='__main__':
    print(is_palindrome('noon'))
    
    print(is_palindrome('racecar'))
    print(is_palindrome('dented'))
    
