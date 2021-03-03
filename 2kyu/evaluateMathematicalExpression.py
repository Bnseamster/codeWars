def calc(string):
    
    try:
        ##adding spaces
        x=0
        while(x < len(string)-1):
            if string[x].isnumeric() and string[x+1].isnumeric():
                pass
            elif string[x].isalpha():
                string = string[:x] + string[x+1:]
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
        if len(string) == 1:
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
    
    return 1

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
        if string[x] == '/':
            
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

### Sample input

# calc(''x'2 + 3 * 4 / 3 - 6 / 3 * 3 + 8')
# calc('1 + 2 * 3 * 3 - 8')
# calc('1 + 2 * 3 * (5 - 2) - 8')
# calc('1 + 2 * 3 * (5 - (3 - 1)) - 8')
# calc('4 + -(1)')
# calc('4 - -(1)')
# calc('4 * -(1)')
# calc('4 / -(1)')
# calc('-1')
# calc('-(-1)')
# calc('-(-(-1))')
# calc('-(-(-(-1)))')
# calc('(((((-1)))))')
# calc('5 - 1')
# calc('5- 1')
# calc('5 -1')
# calc('Random tests')
# calc('-5 - 18 / -62 + 79 + -4 / 80 + -31 / -94')
# calc('-83 / -51 / 68 / 17 - 96 + 4 + 42 / 93')
# calc('-33 * -68 / -42 / -7 / -74 + -69 / -26 - -91')
# calc('-3 - -64 * -94 - 73 + 57 * 45 - 67 + 51')
# calc('-11 - 13 - 30 / -83 + 94 - 7 * -90 * -34')
# calc('-16 * 98 * -68 + -62 + 34 - 90 * -56 * -84')
# calc('-66 + 26 + -27 - 42 + -44 / -89 / -27 / 79')
# calc('73 + -25 - 24 - 79 - 70 - -47 + -60 - 9')
# calc('21 * 93 + 13 - 92 - -21 * 2 / -12 * -72')
# calc('-2 / 1 + 98 - 81 + -97 + 97 * -60 * 72')
# calc('-46 - 42 * -73 * -75 * -46 / 72 - 40 * -70')
# calc('96 / 90 - -42 - 13 + 82 - 36 * -86 / -95')
# calc('63 - -73 / -98 / -99 * 27 - -4 / 74 + -16')
# calc('6 * -54 / -93 * -47 + -71 - 96 / 7 - 17')
# calc('-25 + 34 * -38 * 14 * -80 + 64 - 56 / -25')
# calc('41 - -77 - -67 + 12 - -88 * 28 - 94 * -7')
# calc('-42 + -91 * 93 - -3 + -5 * -66 / -45 + 2')
# calc('47 + -16 + -91 * 66 + 53 + -72 * 16 + 32')
# calc('-22 * -10 - 98 / 53 - -53 + -26 - -52 - -79')
# calc('-95 / 65 + -68 / -33 + -93 / -56 + -100 / 50')
# calc('-96 * -93 * -73 / -42 / -70 * -87 - -79 / -70')
# calc('33 * -27 + -5 * -38 / -87 - -39 + -31 * -63')
# calc('86 / -21 + 38 * 84 + 4 + -95 - 25 / -29')
# calc('-7 - 60 + 85 * -35 / -62 / -93 + 70 + -81')
# calc('32 * 9 - -71 / -56 + -33 * -13 - -20 + -6')
# calc('86 + 18 * -33 * 41 + -54 - 6 + 35 / 98')
# calc('57 / 20 + -76 * -13 - -91 - 69 + 81 - -57')
# calc('-68 * 50 - 42 - -85 * 96 / 27 + -33 + -10')
# calc('99 + -73 * -12 - 50 + -28 / -21 + -98 - 41')
# calc('-42 * -33 * 24 / -94 / -96 + -55 / 41 - -61')
# calc('-6 * 99 + 92 + 81 - -86 * -14 + 38 * -48')
# calc('-45 - -93 + -76 + -25 / 19 * -1 - -7 - -32')
# calc('-41 / -82 * -15 - 84 / 46 - -52 + 78 * -9')
# calc('-33 * -22 + 67 - -14 + -5 + -65 / 77 + 97')
# calc('43 + -43 / 67 / 40 * 89 - 62 - -8 + 46')
# calc('-19 + -18 - 56 + -98 * 41 + -73 - -47 - -72')
# calc('-2 / 24 - -85 * -82 / 34 * 64 - 92 - -13')
# calc('34 + 84 + -84 * 87 / 41 - 78 * 39 + -48')
# calc('-68 - 11 - 47 / -46 - 19 - 4 * 93 / -2')
# calc('-4 + -89 / 23 / 10 / 19 - 4 * 30 * 34')
# calc('11 * -58 + 2 - 91 / -18 - -63 * -20 + 62')
# calc('76 + 93 * -40 - -5 + 76 / -73 + 71 + 71')
# calc('-85 * -41 - -21 - 68 * -8 * 71 * 7 + -84')
# calc('76 - 78 / -15 / 23 - 48 - -76 - 33 * 54')
# calc('25 * 90 * -63 - 71 * -6 / -34 / -93 - 14')
# calc('-44 / 99 - -69 + -76 + 47 - 37 / 12 * -57')
# calc('-7 / 81 / 8 / 5 + -11 - 84 * -86 - -35')
# calc('45 - -5 * 65 + -68 * -1 + -31 / -66 / 63')
# calc('-37 + 69 - -64 - -31 * -83 * -83 - 88 + -33')
# calc('-3 / -50 / 53 / -91 * -48 - 48 + -4 * -69')
# calc('-4 * -10 + 27 * 82 - 98 * 40 - -14 + 13')
# calc('16 - -26 + -63 - -94 / -23 * -17 / -54 + -1')
# calc('90 * 30 / -88 * 48 / -22 + 53 * -43 + 11')
# calc('90 + 68 * 23 + -75 / -13 / -13 - -31 - 10')
# calc('-7 + 99 * 20 + -12 + -43 / 72 / 86 * 82')
# calc('59 * 69 * 80 / -100 / 55 / 57 - -89 * 69')
# calc('33 - -88 + 75 / -98 - -74 * 43 - -50 * -79')
# calc('97 / 36 / -51 / -55 / 61 / -48 / -94 - 22')
# calc('67 * 30 * -51 + -54 + 51 * -84 / -95 + -24')
# calc('36 - -6 * 3 / 88 * -56 - -44 / -8 * -52')
# calc('39 + -23 + 37 * 93 + 94 / 44 + 42 * -34')
# calc('-62 * 13 - 42 / -93 + -65 * 34 * 90 + -30')
# calc('-85 / 96 + 87 / -51 - 37 + 80 / 83 + -33')
# calc('52 * -22 - 18 * -51 / -16 * -100 - -57 + 14')
# calc('-83 / 99 * 24 / -55 - 12 + 18 - -12 + 88')
# calc('-62 - -4 / 84 * 48 / -50 - -81 * 91 / -3')
# calc('88 + 1 + -28 / -16 / 36 + 4 - -50 / 41')
# calc('-97 * -71 / -13 / 27 + 83 + -24 / -19 + 74')
# calc('42 * -61 * 51 * -2 - -81 / -10 - -58 / 46')
# calc('-43 + 1 / 53 * -11 + 65 * -65 / -25 * -89')
# calc('-79 / -78 - 34 * -22 / 38 + -58 * 23 + 99')
# calc('-74 * -60 * -59 / 57 * 71 + -21 / -50 + 64')
# calc('-16 - 3 + -63 + 3 * -41 + -36 - -84 / 89')
# calc('53 + -89 * -99 - 23 * 70 * -18 - -20 * -37')
# calc('-54 + -78 + 15 * 30 / -65 / 22 + 60 + 97')
# calc('-74 + -42 - -62 + -11 / -34 + 31 / -45 / 23')
# calc('81 - 42 - -29 * 13 / 17 - -11 + -97 * -66')
# calc('-18 + 25 + -64 * -54 - -1 * -2 * 81 * -38')
# calc('18 / -22 - -8 + 94 * -21 / -13 - -19 * 14')
# calc('-37 + 41 + -29 - 100 + -36 + -15 / 39 - 16')
# calc('84 + -1 - -39 + -88 * 22 + 93 * 16 + 90')
# calc('4 / 71 + -72 + -78 / 36 / -98 / 44 * 14')
# calc('5 + 51 - -60 / 14 - -67 / 75 / -29 / 59')
# calc('-71 * 40 - 84 - -36 - 84 / 51 / -7 + 1')
# calc('-100 * -37 * 82 / -66 * -9 + 43 / -96 * 39')
# calc('28 + -14 / -35 * -66 + -8 * -61 + 99 * -74')
# calc('84 * -31 + -56 + 59 - 17 - -85 - -94 * -53')
# calc('-63 / -94 * 41 * -80 - -43 - -57 - -66 / -51')
# calc('-91 - -27 * 95 * -62 + -41 / 51 + 91 + 85')
# calc('-92 * -25 / 89 + 34 - -60 - 60 + -65 / 44')
# calc('67 + 36 / -60 * -80 + 68 / 92 * 2 * -10')
# calc('-11 * -54 * 22 - -65 * -80 / -50 * 20 + -41')
# calc('-24 / -25 * 40 - 64 * 27 * 33 / -18 + -80')
# calc('96 / -91 / -75 + 78 / 47 * -24 - -33 / -56')
# calc('66 * -8 / -50 / 4 / 93 + 57 * -1 + -84')
# calc('-39 * 46 - 4 * -98 / -15 - 2 - -1 + -12')
# calc('-84 * 91 / 94 + 68 * -42 + -60 * 81 + 81')
# calc('26 / -71 - 14 * -44 - 51 / 6 * 9 - 61')
# calc('15 - 41 - -27 * 47 + -41 / 83 - -12 - -38')
# calc('53 - -74 + 98 * 40 * 87 + -98 / -62 / 31')
# calc('(-43) / (96 * 90 / (2)) + (-17 + -((((-52 - 40)))) - -35)')
# calc('-(-49) + (-53 + -76 + -(96)) + (46 * -(((-(-60 - -28)))) - -94)')
# calc('(-19) / (-8 + 31 / -(12)) + (-49 * -(((-(95 - 66)))) * 32)')
# calc('-(-90) / (15 + -17 - (68)) - (-64 + ((((-25 / -23)))) / -59)')
# calc('-(83) - (-64 / -42 * -(84)) + (-6 + (((-(-63 / 21)))) * -90)')
# calc('-(37) + (-80 * 8 - (67)) / (88 * -((((-43 - 99)))) - -19)')
# calc('(87) + (-88 + 83 + (85)) * (-2 - -(((-(94 + -99)))) * -83)')
# calc('(52) - (-18 + 68 - (62)) / (-46 - -(((-(-38 + 55)))) - -2)')
# calc('(33) + (-17 / 9 / (37)) - (78 * ((((27 / -46)))) / -85)')
# calc('-(60) - (24 - 90 + -(59)) - (97 * -((((1 * -11)))) + -80)')
# calc('-(87) - (-81 + -14 * -(17)) / (-54 + -((((-28 + -90)))) - 93)')
# calc('(54) * (28 * -48 + (22)) / (75 - (((-(-98 - -14)))) * 65)')
# calc('(66) * (31 * -52 + (55)) + (-66 / (((-(-13 * -57)))) - -37)')
# calc('(70) - (-80 - -50 - (96)) - (93 - -(((-(34 / 54)))) - 1)')
# calc('-(-30) * (5 * -41 - -(44)) - (-85 * -(((-(10 * -15)))) - -8)')
# calc('-(92) - (58 / -53 - (26)) - (38 + -((((69 / -55)))) * -82)')
# calc('-(-89) - (-78 * -67 / (77)) * (98 + -(((-(-88 - 49)))) / -45)')
# calc('-(53) - (65 / -27 + -(91)) - (53 - -((((30 - -2)))) - -82)')
# calc('(35) - (-95 / -84 + (50)) * (-21 * -((((23 - 76)))) * 91)')
# calc('(28) * (21 + -82 - (37)) - (10 * ((((36 - 22)))) + -49)')
# calc('(33) + (-40 + -48 / (66)) / (-58 / -(((-(-5 - -24)))) + -68)')
# calc('(75) + (-23 * -37 + -(98)) / (-54 - ((((-79 * 87)))) + 95)')
# calc('(9) - (9 / 40 - -(2)) + (32 * -(((-(19 / -3)))) / -60)')
# calc('(68) * (85 * -65 + -(19)) * (30 + -((((17 * -76)))) / 2)')
# calc('-(-40) - (11 + -6 + -(45)) + (-62 / ((((91 + -10)))) / 75)')
# calc('-(5) - (-85 + 25 + (30)) + (-24 - ((((49 * 4)))) - -38)')
# calc('-(-3) - (-94 / 47 + -(16)) + (67 - (((-(86 - 84)))) + -41)')
# calc('(56) - (77 - -51 / -(55)) / (60 / -((((82 - 39)))) / 11)')
# calc('(29) + (-1 / -55 - (44)) * (-31 / -(((-(-80 / 68)))) - 98)')
# calc('(-23) * (35 + -82 + -(24)) * (-67 / ((((10 * -11)))) / -14)')
# calc('-(-71) / (74 / -69 + (83)) - (-18 - ((((22 + 76)))) / 63)')
# calc('(33) + (-67 / 51 + (42)) / (-22 / ((((1 / -4)))) - 35)')
# calc('-(34) + (95 + -75 - (59)) + (22 - -((((59 - -14)))) + -45)')
# calc('(-70) - (94 + -41 - -(97)) + (55 / -(((-(53 - 9)))) - 85)')
# calc('(79) - (91 * -99 + (76)) * (-32 * -(((-(-50 * -9)))) - 12)')
# calc('(62) * (-10 + 86 * -(39)) / (70 / ((((26 + 65)))) * 35)')
# calc('(34) * (59 * -1 * (29)) * (-24 * -((((-33 + 57)))) / -30)')
# calc('-(-24) / (-68 * -38 - -(89)) * (34 + -(((-(55 / -70)))) * 31)')
# calc('(43) * (-59 / -97 - (27)) + (-69 - -(((-(75 / 2)))) - -34)')
# calc('(34) - (-86 + -74 - (80)) + (-24 * -((((7 - 59)))) / -61)')
# calc('(-34) / (-6 / 25 / (72)) / (91 - -((((71 * 44)))) + -33)')
# calc('(-15) / (64 * -100 * -(66)) + (81 + ((((-15 + 57)))) + 9)')
# calc('-(-66) * (-6 * 50 / -(18)) - (-67 + -(((-(-48 + -80)))) / 19)')
# calc('(-83) * (24 * -35 - -(50)) - (-1 * -(((-(46 + -53)))) - -93)')
# calc('(51) / (99 - -92 - (28)) / (-29 + -((((32 + -90)))) - 52)')
# calc('(67) * (-55 + 49 - (39)) * (-6 / -((((92 - 25)))) - -92)')
# calc('-(-41) - (64 / 88 * -(1)) - (24 / -((((-35 - -70)))) - -86)')
# calc('(69) * (-72 - 71 + -(65)) / (-6 + (((-(-32 - -23)))) - -21)')
# calc('-(-20) + (6 * -78 - -(61)) / (-14 / ((((-47 + 49)))) / 63)')
# calc('-(-51) - (19 + 64 + -(8)) * (-67 / ((((93 / -96)))) + 8)')
# calc('-(-41) + (24 * -5 - -(87)) / (82 + -((((20 + 60)))) + -26)')
# calc('-(98) * (81 - 11 - (38)) + (94 + -(((-(-38 * 37)))) / -53)')
# calc('(68) + (-30 * -1 * -(44)) / (24 / ((((26 + 67)))) + -29)')
# calc('(25) + (-100 * 48 * (62)) * (-74 / ((((54 + 8)))) / 53)')
# calc('(46) + (-14 * 32 * -(84)) - (12 / -(((-(34 + -84)))) * -21)')
# calc('-(81) / (-92 * -60 - (48)) + (-16 / -(((-(84 + -19)))) + -4)')
# calc('(-90) - (90 - 12 / -(18)) - (-82 - (((-(53 / 69)))) + -18)')
# calc('-(-5) / (-33 / 83 / -(43)) / (-58 - (((-(89 / -46)))) / 23)')
# calc('(7) / (-56 - 60 + -(69)) * (33 - ((((-21 / -67)))) + -56)')
# calc('-(-25) / (-11 - 28 / (96)) - (-44 - (((-(38 + 56)))) * -70)')
# calc('(-31) / (-36 * 34 / (23)) - (-70 / ((((61 + 86)))) - 69)')
# calc('(-4) * (73 / -37 + (40)) / (-96 + ((((-99 + 3)))) / 82)')
# calc('-(-62) / (-36 - 60 - (43)) * (-68 * -(((-(94 + 2)))) * 11)')
# calc('-(15) - (10 + 75 - (47)) + (47 + ((((-46 / 41)))) * 71)')
# calc('-(-19) * (-64 / -19 + -(40)) / (32 / -(((-(43 / -20)))) * 78)')
# calc('-(-28) * (62 - 57 - -(42)) + (-97 / (((-(-15 / -78)))) - -3)')
# calc('-(-9) / (31 + 81 - -(7)) / (19 + ((((-2 + 36)))) + -85)')
# calc('(24) / (-25 * 82 / -(20)) - (-60 - ((((51 * -75)))) - -52)')
# calc('-(-71) - (32 + -44 * (93)) + (-37 - (((-(-79 / -40)))) * -68)')
# calc('(64) * (-21 / 50 - -(21)) * (-21 * -(((-(20 * -43)))) + -80)')
# calc('-(-89) * (34 * -32 + -(15)) / (-61 + -(((-(56 * 62)))) + -40)')
# calc('-(61) + (69 * 65 + -(66)) + (75 - (((-(52 / -74)))) / -84)')
# calc('-(37) * (97 * 21 * -(48)) / (-67 / ((((50 * -70)))) - -78)')
# calc('-(78) / (85 - -97 + -(55)) / (99 - (((-(-46 + -71)))) * -84)')
# calc('-(63) / (-5 / 100 - (68)) + (81 - ((((70 - 53)))) / -100)')
# calc('(36) * (-42 - 97 - (46)) * (14 / (((-(-81 / 56)))) * 24)')
# calc('(45) + (58 + 39 + (25)) + (90 + (((-(38 - 95)))) - 18)')
# calc('(-51) / (-62 - -80 / -(88)) - (77 + -((((-89 - -51)))) + 12)')
# calc('(-76) / (-68 - -73 * (6)) / (-38 / -((((34 * 99)))) / -74)')
# calc('(-4) + (8 + -98 + (99)) / (-2 / -(((-(87 * 58)))) / 32)')
# calc('-(-48) * (40 - 70 - -(34)) + (99 - ((((-75 * -87)))) / 77)')
# calc('(-75) / (97 + -73 / -(49)) - (-90 / -(((-(7 + 12)))) - 90)')
# calc('-(19) + (-36 - 75 - (85)) + (19 / -(((-(63 + 50)))) - -97)')
# calc('-(69) / (43 / -37 - (99)) + (3 / ((((50 + 59)))) + 8)')
# calc('-(-66) * (86 + -100 / (70)) - (18 + -(((-(-62 * -63)))) / -37)')
# calc('(-7) + (51 + -6 - (82)) + (-50 * ((((99 * -71)))) + -97)')
# calc('-(69) + (-56 - -3 - -(23)) + (-26 / -((((8 - -50)))) - 28)')
# calc('-(44) * (74 * -86 * -(17)) / (26 * ((((88 * -80)))) - -22)')
# calc('-(87) / (-57 - -73 - -(41)) - (74 - -(((-(91 / 96)))) + 86)')
# calc('(-27) - (-38 * -38 + (20)) - (-65 + -(((-(23 * -91)))) - -90)')
# calc('-(58) + (-87 * -97 + -(86)) - (94 - (((-(-91 - -37)))) + 49)')
# calc('(-57) + (-64 + 33 + (25)) / (-93 * -((((-90 + 73)))) / 3)')
# calc('-(-33) * (-11 + -64 * (17)) / (-15 - -((((-58 - -51)))) - 14)')
# calc('(10) * (-29 - 1 - (41)) + (22 / -((((85 - -8)))) * -96)')
# calc('-(-33) * (93 - 86 * (64)) * (-43 / -((((81 / -67)))) * -28)')
# calc('-(39) - (-40 * 31 / (7)) * (91 + (((-(14 * 1)))) + -13)')
# calc('-(84) + (86 / 53 * -(36)) - (-19 * -(((-(10 * 63)))) * 3)')
# calc('-(22) / (90 * 52 / (41)) / (-92 - -(((-(86 - -38)))) - -47)')
# calc('-(57) / (64 * 39 / -(34)) + (77 * (((-(49 * 46)))) + 51)')
# calc('(100) - (-94 / -98 / (42)) - (-95 * ((((-17 / 90)))) / 8)')
# calc('-22- 33- -45- 69')
# calc('53- 100- -50- 12')
# calc('-34- -53- -63- -45')
# calc('-17- -40- 49- -60')
# calc('32- 6- -42- 96')
# calc('-89- 38- -69- 4')
# calc('-67- 19- 78- 81')
# calc('-80- 5- 55- 89')
# calc('5- 72- 78- 80')
# calc('-31- -87- -90- -6')
# calc('-39- 36- 87- 3')
# calc('31- -11- -30- 4')
# calc('96- 3- -70- -98')
# calc('-32- -35- 98- 58')
# calc('-67- 27- -15- 37')
# calc('-4- -36- -8- 19')
# calc('-45- 67- 61- -97')
# calc('96- 94- 42- -11')
# calc('1- 3- 21- 45')
# calc('-3- 11- -50- 41')
# calc('71- 77- 33- 98')
# calc('90- -86- 96- 28')
# calc('8- 50- 30- -31')
# calc('29- 36- -55- 41')
# calc('-99- 56- 2- -26')
# calc('-73- 27- -12- -59')
# calc('-71- 44- 53- 37')
# calc('50- -36- 33- 93')
# calc('42- -70- -60- 36')
# calc('40- 28- -25- 70')
# calc('-74- -22- 77- 82')
# calc('-76- 49- 53- -9')
# calc('-26- -51- -60- -33')
# calc('64- 33- 23- 6')
# calc('-16- -8- 13- 27')
# calc('-100- 95- 66- 20')
# calc('-96- 50- -90- -87')
# calc('-55- -84- 29- -95')
# calc('-13- 90- -58- 17')
# calc('87- -4- -13- 40')
# calc('9- -7- 19- -56')
# calc('-47- -96- -67- -45')
# calc('-42- 23- 16- 81')
# calc('-73- -45- -62- 5')
# calc('-77- -30- 21- 15')
# calc('-42- 72- 81- -11')
# calc('74- 65- -76- 37')
# calc('-79- -68- -8- 26')
# calc('10- 61- 35- -55')
# calc('-28- -72- 26- 75')
# calc('33- -48- 61- -59')
# calc('35- -43- -44- -56')
# calc('-12- -79- -79- 31')
# calc('-20- -57- 14- 24')
# calc('-46- 23- -45- -88')
# calc('71- 53- -30- 42')
# calc('22- -8- 79- 58')
# calc('-88- -35- -63- 99')
# calc('-63- -24- -91- -77')
# calc('-48- -79- 55- 13')
# calc('-97- 73- 97- -92')
# calc('95- 59- 75- -17')
# calc('7- 83- 28- -30')
# calc('-23- -45- 37- 21')
# calc('-16- 12- 33- 72')
# calc('-56- -29- 75- -92')
# calc('-87- 10- -79- 96')
# calc('-95- -20- 73- 93')
# calc('65- 95- -31- 58')
# calc('-2- -46- 10- -79')
# calc('30- -44- -6- 71')
# calc('-48- -81- 95- -92')
# calc('10- 40- -20- -28')
# calc('-41- 91- -16- 78')
# calc('-44- -52- -31- -3')
# calc('4- 70- 85- -60')
# calc('-39- 84- 31- 55')
# calc('48- -69- 37- -16')
# calc('48- 7- -54- 58')
# calc('-40- 46- 74- 54')
# calc('-58- 1- 24- -66')
# calc('-11- -96- 86- 35')
# calc('-41- -7- -38- 32')
# calc('20- 21- 70- -91')
# calc('-23- 50- -30- 88')
# calc('9- -1- -96- 89')
# calc('64- 92- -14- -63')
# calc('-40- 50- 9- 83')
# calc('-95- 70- 99- 4')
# calc('-25- 39- 65- -72')
# calc('-98- 11- 14- -1')
# calc('74- -58- 22- 84')
# calc('-36- 57- 16- 23')
# calc('61- 45- 2- 42')
# calc('30- -90- 65- -16')
# calc('50- 45- 96- -29')
# calc('57- 59- -56- -14')
# calc('-56- 98- 18- 79')
# calc('39- 26- -48- 2')
