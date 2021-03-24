def find_outlier(integers):
    countE = 0
    countO = 0
    
    
    for int in integers:
        if int%2 == 0:
            countE += 1
        elif int%2 == 1:
            countO += 1
        
        
        if countE > 1:
            for num in integers:
                if num % 2 == 1:
                    return num
        
        elif countO > 1:
            for num in integers:
                if num % 2 == 0:
                    return num