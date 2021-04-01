from collections import Counter

def validate_battlefield(field):
    neighborsD = [(1,0)]
    neighborsR = [(0,1)]
    neighborsDiag = [(-1,1),(-1,-1),(1,-1),(1,1)]
    shipTracker = Counter({'b':1,'c':2,'d':3,'s':4})
    directionSet = set()
    seenSet = set()
    count = 0
    
    def checkDiag(i,j):
        
        if 0 <= i + 1 < len(field) and 0 <= j + 1 < len(field[0]):
            if field[i + 1][j + 1] == 1:
                return False
        
        if 0 <= i + 1 < len(field) and 0 <= j - 1 < len(field[0]):
            if field[i + 1][j - 1] == 1:
                return False
        
        return True
            
        
    
    def dfs(i,j,count):
        
        if not checkDiag(i,j):
            return 5
        
        if 0 <= i + 1 < len(field):
            if field[i + 1][j] == 1:
                directionSet.add('D')
                seenSet.add((i+1, j))
                count = dfs(i+1,j,count + 1)
            
        if 0 <= j + 1 < len(field[0]):
            if field[i][j + 1] == 1:
                directionSet.add('R')
                seenSet.add((i,j+1))
                count = dfs(i,j+1,count + 1) 
        
        if len(directionSet) > 1:
            return 5

        return count
            
        
         
        
    for i,row in enumerate(field):
        for j,spot in enumerate(row):
            if spot == 1 and (i,j) not in seenSet:
                seenSet.add((i,j))
                count = 1
                count = dfs(i,j,count)
                if count > 4:
                    return False
                elif count == 4:
                    shipTracker.update({'b':-1})
                elif count == 3:
                    shipTracker.update({'c':-1})
                elif count == 2:
                    shipTracker.update({'d':-1})
                elif count == 1:
                    shipTracker.update({'s':-1})
                directionSet = set()
                count = 0
    for key, val in shipTracker.items():
        if val != 0:
            return False 

    return True