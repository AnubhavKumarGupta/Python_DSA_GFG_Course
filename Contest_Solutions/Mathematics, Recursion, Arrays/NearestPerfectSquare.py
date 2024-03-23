#User function Template for python3

def nearestPerfectSquare(n):
    #Your code here
    import math

    abovenumBER = math.ceil(math.sqrt(n+1)) * math.ceil(math.sqrt(n+1))
    belownumBER = math.floor(math.sqrt(n-1)) * math.floor(math.sqrt(n-1))
    
    difference_1 = n - abovenumBER
    difference_2 = belownumBER - n
    
    if difference_1 == difference_2:
        return belownumBER
    elif difference_1 > difference_2:
        return abovenumBER
    else:
        return belownumBER


