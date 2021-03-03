def y(x):
    a = (2*x+1)
    return a

def z(x):
    a = (3*x+1)
    return a



def dbl_linear(n):
    u = [1]

    while len(u) < n:
        for c in range(len(u)):
            u.append(y(u[c]))
            u.append(z(u[c]))
                    
        u = sorted(list(set(u)))
    max = u[-1]
    
    
    
    
    new = []
    for c in range(len(u)):
        yi=y(u[c])
        zi=z(u[c])
        
        
        if (yi < max):
            new.append(y(u[c]))
        elif (zi < max):
            new.append(z(u[c]))
    
    
    while True:
        for c in range(len(new)):
            yi = y(u[c])
            zi = z(u[c])
            
            
            if yi not in u and (yi < max):
                new.append(y(u[c]))
            elif zi not in u and (zi < max):
                new.append(z(u[c]))
        u = u + new
        sorted(new)
        if(len(new) == 0):
            break
        new = []    
            
        
                    
    u = sorted(list(set(u)))

    print(n)
    return u[n] 

dbl_linear(10)