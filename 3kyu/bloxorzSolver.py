level = []

def blox_lover(ar):

    #

    #get coordinates of h & b
    
    #get delta between hole and block 
    def getDirection(h,b):
        dx = h[0] -b[0]
        dy = h[1] -b[1]

        if Math.abs(dx) > math.abs(dy):
            if dx > 0:
                return 'R'
            else:
                return 'L'
        else math.abs(dx) > math.abs(dy):
            if dy > 0:
                return 'D'
            else:
                return 'U'
    