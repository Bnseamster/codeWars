def is_divisible(n,x,y):
    #your code here

    if type(n) != int:
        raise Exception(f'Invalid input of type {type(n)} should be of type {int}')

    if type(x) != int:
        raise Exception(f'Invalid input of type {type(x)} should be of type {int}')
    if type(y) != int:
        raise Exception(f'Invalid input of type {type(y)} should be of type {int}')
    
    return True if n%x ==0 and n%y == 0 else False