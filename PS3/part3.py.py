''' Next, implement the function getAvailableLetters that takes in one parameter -
a list of letters, lettersGuessed.
This function returns a string that is comprised of lowercase English letters
- all lowercase English letters that are not in lettersGuessed.'''

'''>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz''''

'''Hint: You might consider using string.ascii_lowercase,
 which is a string comprised of all lowercase letters:

>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz'''

import string
words = string.ascii_lowercase

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    for i in words:
        if i not in lettersGuessed:
           result +=i
    return result