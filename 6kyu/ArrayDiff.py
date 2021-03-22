def array_diff(a, b):
    setB = set(b)
    aCopy = [num for num in a]
    for num in aCopy:
        if num in setB:
            a.remove(num)
    return a