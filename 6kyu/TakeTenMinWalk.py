def is_valid_walk(walk):
    countEW = 0
    countNS = 0
    
    for direction in walk:
        if direction == 'w':
            countEW -= 1
        elif direction == 'e':
            countEW += 1
        elif direction == 'n':
            countNS += 1
        elif direction == 's':
            countNS -= 1         
    
    
    return True if len(walk) == 10 and countNS == 0 and countEW == 0 else False