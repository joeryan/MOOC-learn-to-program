

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

def is_palindrome3(s):
    """ (str) -> bool
    >>> is_palindrome3('noon')
    True
    >>> is_palindrome3('racecar')
    True
    >>> is_palindrome3('dented')
    False
    """
    # ensure string is all lowercase
    s = s.lower()
    # set counters to beginning and end of string
    i, j = 0, len(s)-1
    # move through string comparing characters from either end
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1

    # return true if middle was reached and characters matched
    return i >= j


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
        print(word, "is palindrome (1)", is_palindrome1(word))
        print(word, "is palindrome (2)", is_palindrome2(word))
        print(word, "is palindrome (3)", is_palindrome3(word))
        
