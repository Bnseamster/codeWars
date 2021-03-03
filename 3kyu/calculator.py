class Calculator(object):
    
    def evaluate(self, string):
        string = string.split()
        string = [float(x) if x.isnumeric() else x for x in string]
        
        if len(string) == 1:
            return string[0]


        bounds = findParen(string)

        while (bounds[0] != None):
            while bounds[0] == 'r':
                string = bounds[1]
                bounds = findParen(string)

            bounds = findParen(string)
            while bounds[0] == 'r':
                string = bounds[1]
                bounds = findParen(string)
                

            string = divMult(string,bounds)

            bounds = findParen(string)
            while bounds[0] == 'r':
                string = bounds[1]
                bounds = findParen(string)
                

            string = addSub(string,bounds)

        string = divMult(string)
        string = addSub(string)



      
            
    
        return float(string[0])


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

def divMult(string, bounds=[None]):
    if bounds[0] == None:
        bounds = [0, len(string)]
    
    x = bounds[0]
    
    while x < bounds[1]:
        if string[x] == '/':
            
            #replace the xth number
            string[x-1] = str(float(string[x-1]) / int(string[x + 1]))
            
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

def addSub(string, bounds=[None]):
    if bounds[0] == None:
        bounds = [0, len(string)]
    
    x= bounds[0]

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

### Sample input
Calculator().evaluate('127')