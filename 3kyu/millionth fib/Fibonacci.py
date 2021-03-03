import math

def fib(n, store = {'0':0,'1':1,'2':1}):
#   string rep of number
    sn = str(n)

    if (sn in store):
        return store[sn]

    if n <= 0:
        arr = [0,1]
        n *= -1 

        for ele in range (0,n):
            nextNum = arr[1] - arr[0]
            arr[1] = arr[0]
            arr[0] = nextNum
            
        return nextNum
            
    
    else:
    
        arr = [1,1]
        
        for ele in range(2,n):
            nextNum = arr[-1] + arr[-2]
            arr[-2] = arr[-1]
            arr[-1] = nextNum
        
        return arr[-1]




def f(n):

    Phi = (math.sqrt(5)+1)/2
    phi = Phi - 1

    ans = ((Phi**n) -((-1)*phi)**n)/math.sqrt(5)

    return print(math.floor(ans))

def solution(number):
    
  sum=0
    
  for x in range(number):
    print(((x) % 3) == 0)
    if ((x ) % 3) == 0 or ((x) % 5) == 0:
        sum += x
        
  return print(sum)

solution(10)