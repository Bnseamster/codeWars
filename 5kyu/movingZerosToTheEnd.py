def move_zeros(array):
    numOfZeros = array.count(0)
    appendZeros = [0] * numOfZeros
    
    for _ in range(numOfZeros):
        array.remove(0)
        
    
    return array + appendZeros