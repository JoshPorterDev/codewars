from math import sqrt

def test(number):
    """ Return the next square if number is a square, otherwise return -1 """
    sq = sqrt(number)
    if int(sq) * int(sq) == number:
        return int((sq + 1) * (sq + 1))

    else:
        return -1

print(test(81))