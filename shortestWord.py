def find_short(s):
    """ Return the length of the shortest word in the given string """
    stringArray = s.split() # Turn the list into an array with each word in the list represented by a different item in the array
    lenOfWords = []
    for word in stringArray:
        lenOfWords.append(len(word))

    lenOfWords.sort() # sorting the list by the default ascending order
    return lenOfWords[0] # Returning the first item in the list, which represents the len of the shortest word in the sting

