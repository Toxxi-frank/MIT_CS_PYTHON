# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    if word not in wordList:
        return False

    hand_copy = hand.copy()

    for char in word:
        if char in hand:
            hand_copy[char] -= 1
            if hand_copy[char] < 0:
                return False
        else:
            return False

    return True
