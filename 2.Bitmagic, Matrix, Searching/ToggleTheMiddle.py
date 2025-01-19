import math
def toggleTheMiddle(n):
    numberOfBits=1+math.floor(math.log2(n))
    if numberOfBits%2!=0:
        n=n^(1<<(numberOfBits//2))
    else:
        n=n^(1<<(numberOfBits//2))
        n=n^(1<<((numberOfBits//2)-1))
    return n