import string

def toJadenCase(test):
    """ Convert a given string into jaden case, capitalizing the first letter of each word """
    return string.capwords(test)

print(toJadenCase("How can mirrors be real if our eyes aren't real"))

