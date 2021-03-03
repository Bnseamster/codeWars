def calculate(string):
    
    try:
        ##adding spaces
        x=0
        while(x < len(string)-1):
            if string[x].isnumeric() and string[x+1].isnumeric() or string[x+1]== '.':
                if string[x+1] == '.':
                    x += 1
                pass
            elif string[x].isalpha():
                string = string[:x] + string[x+1:]
                return '400: Bad request'
            elif (string[x+1] != ' ' and string[x] != ' '):    
                string = string[:x+1] + ' ' + string[x+1:]
                x+=1            

            x += 1
        ##change string to array split by spaces
        string = string.split()
        ##combine numbers if next to eachother
        string = [float(x) if x.isnumeric() else x for x in string]

        string = negCheck(string)
        
        ##if array is one number calculation is done return number
        if len(list(string)) == 1:
            return float(string[0])

        bounds = findParen(string)

        #checks for parentheses and solves within parentheses bounds
        while (bounds[0] != None):
            while bounds[0] == 'r':
                string = bounds[1]
                bounds = findParen(string)
            bounds = findParen(string)

            string = negCheck(string)

            while bounds[0] == 'r':
                string = bounds[1]
                bounds = findParen(string)

            string = negCheck(string)   
            string = divMult(string,bounds)
            bounds = findParen(string)


            while bounds[0] == 'r':
                string = bounds[1]
                bounds = findParen(string)
            string = negCheck(string)
            string = divMult(string,bounds)    
            string = addSub(string,bounds)
        #after there are no more parentheses solve the final equation 
        string = negCheck(string)
        string = divMult(string)
        string = addSub(string)



        return float(string[0])
    except:
        pass
    
    return '400: Bad request'

#finds parentheses in array
def findParen(string):
    x = 0

    while x < len(string):
        if string[x] == '(':
            left = x
        elif string[x] == ')':
            right = x

            if right - left == 2:
                string[left] = string[left+1]
                altStr = string[:left+1] + string[right + 1:]
                
                return ["r", altStr]
        
            return [left,right]
        
        x += 1
    
    return [None]

#multiplies and divides numbers on either side of * / within bounds
def divMult(string, bounds=[None]):
    if bounds[0] == None:
        bounds = [0, len(string)]
    
    x = bounds[0]
    try:
        bounds[1] = string.index(')', x, bounds[1])
    except:
        pass
    while x < bounds[1]:
        if string[x] == '$':
            
            #replace the xth number
            string[x-1] = str(float(string[x-1]) / float(string[x + 1]))
            
            #remove x & x+1
            string = string[:x] + string[x+2:]

            bounds[1] -= 2
                

        elif string[x] == '*':
            #replace the xth number
            string[x-1] = str(float(string[x-1]) * float(string[x + 1]))
            
            #remove x & x+1
            string = string[:x] + string[x+2:]
            bounds[1] -= 2
            
        else:
            x += 1

    return string

#add and subtract numbers on either side of - or + within bounds
def addSub(string, bounds=[None]):
    if bounds[0] == None:
        bounds = [0, len(string)]
    
    x= bounds[0]
    try:
        bounds[1] = string.index(')', x, bounds[1])
    except:
        pass

    while x < bounds[1]:
        if string[x] == '+':
            
            #replace the xth number
            string[x-1] = str(float(string[x-1]) + float(string[x + 1]))
            
            #remove x & x+1
            string = string[:x] + string[x+2:]
            bounds[1] -= 2
            
        elif string[x] == '-':
            #replace the xth number
            string[x-1] = str(float(string[x-1]) - float(string[x + 1]))
            
            #remove x & x+1
            string = string[:x] + string[x+2:]
            bounds[1] -= 2
            
        else:
            x += 1
    
    return string

def negCheck(string, operation = ['(','+','*','-','/']):
    ##checking for negative numbers
    x=0
    
    while(x < len(string)):
        if string[x] == '-' and string[x+1] != '(' and ((string[x-1] in operation) or (x==0)):
            string[x] = str(float(string[x+1])*float(-1))
            string = string[:x+1] + string[x+2:]
        
        x += 1
        altStr = string
    return altStr

calculate('1.1')