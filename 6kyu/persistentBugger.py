from functools import reduce

def persistence(n):
    
    count = 0
    
    while len(str(n)) > 1:
        n = reduce(lambda a,b: int(a)*int(b), str(n))
        count +=  1
    return count