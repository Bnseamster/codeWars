from functools import reduce

def square_sum(numbers):
    return reduce(lambda y,x: y + x**2, numbers, 0)