def _if(bool, funct1, funct2):
    """ 
    Takes in a logical test and two funtions as parameters
    Runs the correct function based on the bool of the logical test
    """
    if bool == True:
        funct1()
    elif bool == False:
        funct2()

# Testing

def truthy():
    print("True")

def falsey():
    print("False")

_if(True, truthy, falsey)