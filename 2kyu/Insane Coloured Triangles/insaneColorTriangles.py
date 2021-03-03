def triangle(row):
    tempRow = ''

    i=0
    def color(str):
        if (str[0] == str[1]):
            return str[0]
        elif(str.find('G') == -1):
            return 'G'
        elif(str.find('B') == -1):
            return 'B'
        elif(str.find('R') == -1):
            return 'R'
      
    
    while(len(row) > 1):
        if len(tempRow) == len(row) -1:
            i == 0
            row = tempRow
            tempRow = ''
        else:
            tempRow = tempRow + color(row[i:i+2])
            
    return row[0]

triangle('RRR')


def efficient(row):
    n= #row number
    while n-1 > 7