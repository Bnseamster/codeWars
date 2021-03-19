def digital_root(n):
    
    n =str(n)
    def find(num):
        summation = 0

        if len(str(num)) == 1:
            return int(num)
        for d in str(num):

            summation += int(d)
        return find(summation)
        
    return find(n)