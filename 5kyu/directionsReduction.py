def dirReduc(arr):
    directionStack =[]
    
    dirDict = {
        'NORTH':'SOUTH',
        'SOUTH':'NORTH',
        'EAST':'WEST',
        'WEST':'EAST'
    }
    
    for dir in arr:
        if len(directionStack) > 0 and directionStack[-1] == dirDict[dir]:
            del directionStack[-1]
            continue
            
        directionStack.append(dir)
        
    return directionStack
            