''' Next, implement the function getGuessedWord that takes in two parameters -
a string, secretWord, and a list of letters, lettersGuessed.
This function returns a string that is comprised of letters and underscores,
based on what letters in lettersGuessed are in secretWord.
This shouldn't be too different from isWordGuessed!'''

'''>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e''''


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ''
    for i in secretWord:
        if i in lettersGuessed:
            word +=i
        else:
            word += ' _'
    return word
