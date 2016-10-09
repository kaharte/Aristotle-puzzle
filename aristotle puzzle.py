#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      KatieHarte
#
# Created:     23/07/2016
# Copyright:   (c) KatieHarte 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#.........(1 )(2 )(3 )
#.......(4 )(5 )(6 )(7 )
#.....(8 )(9 )(10)(11)(12)
#.......(13)(14)(15)(16)
#.........(17)(18)(19)
#
#
#

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
g3position = [[1, 2, 3], [3, 7, 12], [12, 16, 19], [19, 18, 17], [17, 13, 8], [8, 4, 1]]
h4position = [[2, 5, 9, 13], [2, 6, 11, 16], [7, 6, 5, 4], [7, 11, 15, 18], [16, 15, 14, 13], [18, 14, 9, 4]]
i5position = [[8, 9, 10, 11, 12], [1, 5, 10, 15, 19], [3, 6, 10, 14, 17]]
sideNumbers = [1, 2, 3, 4, 5, 6]

#all possible sets of 3 numbers that add up to 38
threes = []
twos = []

for x in A:
    C = []
    for y in A:
        if y > x:
            C.append(x)
            C.append(y)
            twos.append(C)
            C = []

print("twos = ", twos)

for x in twos:
    tempTwos = x
    for y in A:
        if sum(x) + y == 38 and y not in x:
            tempTwos.append(y)
            threes.append(tempTwos)

threesCheck = []
sortedThrees = []

for x in threes:
    b = sorted(x)
    sortedThrees.append(b)

for x in sortedThrees:
    if x not in threesCheck:
        threesCheck.append(x)


print("threes = ", threes)
print("threesCheck = ", threesCheck)
print(len(threes))
print(len(threesCheck))

borderNumbers = []
allThrees = []

# 1 and 2 cannot be on corners
for x in threesCheck:
    tempList1 = []
    tempList1.append(x[0])
    tempList1.append(x[1])
    tempList1.append(x[2])
    allThrees.append(tempList1)
    tempList2 = []
    tempList2.append(x[0])
    tempList2.append(x[2])
    tempList2.append(x[1])
    allThrees.append(tempList2)
    tempList3 = []
    tempList3.append(x[1])
    tempList3.append(x[0])
    tempList3.append(x[2])
    allThrees.append(tempList3)
    tempList4 = []
    tempList4.append(x[1])
    tempList4.append(x[2])
    tempList4.append(x[0])
    allThrees.append(tempList4)
    tempList5 = []
    tempList5.append(x[2])
    tempList5.append(x[0])
    tempList5.append(x[1])
    allThrees.append(tempList5)
    tempList6 = []
    tempList6.append(x[2])
    tempList6.append(x[1])
    tempList6.append(x[0])
    allThrees.append(tempList6)


print("allThrees: ", allThrees)
print(len(allThrees))

for x in allThrees:
    keepGoing = True
    borderNumbers = []
    #while keepGoing == True:
    for a in x:
        borderNumbers.append(a)
    corner0 = borderNumbers[0]
    corner1 = borderNumbers[2]
    for y in allThrees:
        if y[0] == corner1 and y[1] not in borderNumbers and y[2] not in borderNumbers:
            borderNumbers.append(y[1])
            borderNumbers.append(y[2])
            corner2 = y[2]
            for z in allThrees:
                if z[0] == corner2 and z[1] not in borderNumbers and z[2] not in borderNumbers:
                    borderNumbers.append(z[1])
                    borderNumbers.append(z[2])
                    corner3 = z[2]
                    for a in allThrees:
                        if a[0] == corner3 and a[1] not in borderNumbers and a[2] not in borderNumbers:
                            borderNumbers.append(a[1])
                            borderNumbers.append(a[2])
                            corner4 = a[2]
                            print('foursides: ', borderNumbers)
                            if len(borderNumbers) != 9:
                                print('ERROR ERROR')
                            for b in allThrees:
                                if b[0] == corner4 and b[1] not in borderNumbers and b[2] not in borderNumbers:
                                    borderNumbers.append(b[1])
                                    borderNumbers.append(b[2])
                                    corner5 = b[2]
                                    for c in allThrees:
                                        if c[0] == corner5 and c[1] not in borderNumbers and c[2] == corner0:
                                                borderNumbers.append(c[1])
                                                borderNumbers.append(c[2])
                                                print('answer: ',borderNumbers)






