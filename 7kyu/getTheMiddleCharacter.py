import math
def get_middle(s):
    if len(s)%2 == 0:
        return s[math.floor((len(s)/2) - 1):math.floor(len(s)/2)+1]
    else:
        return s[math.floor((len(s)-1)/2)]
        