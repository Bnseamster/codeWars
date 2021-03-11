import math
def get_middle(s):
        return s[math.floor((len(s)/2) - 1):math.floor(len(s)/2)+1] if len(s)%2 == 0 else s[math.floor((len(s)-1)/2)]
        