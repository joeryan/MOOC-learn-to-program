

def is_palindrome1(s):
    """ (str) -> bool
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    """
    # make sure the string is all lowercase
    s=s.lower()
    # test for palindrome by comparing to a reversed copy of the string
    return s==reverse(s)

def is_palindrome2(s):
    """ (str) -> bool
    >>> is_palindrome2('noon')
    True
    >>> is_palindrome2('racecar')
    True
    >>> is_palindrome2('dented')
    False
    """
    # make sure the string is all lowercase
    s=s.lower()
    # set n to only calculate s.len() once
    n = len(s)
    # compare first half of string with reverse of second half
    # omit middle char for odd length strings with int division
    return s[:n//2] == reverse(s[n-n//2:])


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
        # push each letter onto the front of rev
        rev=letter+rev
        
    return rev


if __name__=='__main__':
    # if program run as stand alone, test each palindrome
    test_words=['noon', 'racecar', 'NoOn', 'dented']
    for word in test_words:
        print (word, 'is palindrome', is_palindrome1(word))
        print(word, 'is palindrome', is_palindrome2(word))
    
