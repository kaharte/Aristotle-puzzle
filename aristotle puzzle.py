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

import itertools

#.........(A )(B )(C )
#.......(D )(E )(F )(G )
#.....(H )(I )(J )(K )(L )
#.......(M )(N )(O )(P )
#.........(Q )(R )(S )
#
#
#

A1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
Aset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
position = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
g3position = [['a', 'b', 'c'], ['c', 'g', 'l'], ['l', 'p', 's'], ['s', 'r', 'q'], ['q', 'm','h'], ['h', 'd', 'a']]
h4position = [['b', 'e', 'i', 'm'], ['b', 'f', 'k', 'p'], ['g', 'f', 'e', 'd'], ['g', 'k', 'o', 'r'], ['p', 'o', 'n', 'm'], ['r', 'n', 'i', 'd']]
i5position = [['a', 'e', 'j', 'o', 's'], ['c', 'f', 'j', 'n', 'q'], ['l', 'k', 'j', 'i', 'h']]
sideNumbers = [1, 2, 3, 4, 5, 6]
corePositions = ['e', 'f', 'i', 'j', 'k', 'n', 'o']
sidePositions = ['a', 'b', 'c', 'g', 'l', 'p', 's', 'r', 'q', 'm', 'h', 'd']

#all possible sets of 3 numbers that add up to 38
threes = []
twos = []

for x in A1:
    C = []
    for y in A1:
        if y > x:
            C.append(x)
            C.append(y)
            twos.append(C)
            C = []

#print("twos = ", twos)

for x in twos:
    tempTwos = x
    for y in A1:
        if sum(x) + y == 38 and y not in x:
            tempTwos.append(y)
            threes.append(tempTwos)

threesCheck = []
sortedThrees = []

for x in threes:
    b = sorted(x)
    sortedThrees.append(b)

# creates a list of every possible set of 3 numbers adding to 38 w/o duplicates
for x in sortedThrees:
    if x not in threesCheck:
        threesCheck.append(x)


#print("threes = ", threes)
#print("threesCheck = ", threesCheck)
#print(len(threes))
#print(len(threesCheck))

borderNumbers = []
allThrees = []

# 1 and 2 cannot be on corners

# creates a list of every permutation of sets of 3 numbers adding to 38
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


#print("allThrees: ", allThrees)
#print(len(allThrees))

count2 = 0
bNumList = [] #List of all sets of perimiter solutions

for x in allThrees:
    #keepGoing = True
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
##                            print('foursides: ', borderNumbers)
##                            if len(borderNumbers) != 9:
##                                print('ERROR ERROR')
                            for b in allThrees:
                                if b[0] == corner4 and b[1] not in borderNumbers and b[2] not in borderNumbers:
                                    borderNumbers.append(b[1])
                                    borderNumbers.append(b[2])
                                    corner5 = b[2]
                                    for c in allThrees:
                                        if c[0] == corner5 and c[1] not in borderNumbers and c[2] == corner0:
                                            borderNumbers.append(c[1])
                                            borderNumbers.append(c[2])
##                                            newBN = borderNumbers[:13]
                                            if len(borderNumbers) == 13:
                                                newBN = borderNumbers[:]
##                                                print(len(newBN))
                                                #print('newBN: ', newBN)
##                                                count2 += 1
                                                #print('answer: ',borderNumbers)
                                                bNumList.append(newBN)
                                            else:
                                                pass

bNumList.sort()
print("bNumList", bNumList)
#bNumList == all possible sets of border solutions
for a in bNumList:
    count2 +=1
    #print(a)

print("number of possible borders: ", count2)

coreNumbers = []

#corePPermutations = itertools.permutations(corePositions)
#print([x for x in itertools.permutations(corePositions)])

allPairings = []

for x in bNumList:
    y = x[:12]

    #dictionary of possible border solution numbers mapped with positions
    borderDict = dict(zip(sidePositions, y))
    #print("borderDict: ", borderDict)
    #set of numbers inside the core, assuming previous border number solution
    coreNumbers = Aset - set(x)
    print("coreNumbers: ", coreNumbers)

    """newPerimiter = {}
    count3 = 0
    for c in x[:12]:
        newPerimiter[sidePositions[count3]] = c
        count3 += 1
    coreNumbers =[]
    newCore = {}
    count = 0
    for y in A1:
        if y not in x:
            coreNumbers.append(y)"""
    tuple(coreNumbers)
    #print("itertools.permutations(coreNumbers): ", [x for x in itertools.permutations(coreNumbers, 7)])

    for z in [x for x in itertools.permutations(coreNumbers, 7)]:
        #print("This is z: ", z)
        #z is possible set of core numbers
        totalDict = borderDict.copy()
        #dictionary of possible core solutions mapped with positions
        corePairings = dict(zip(corePositions, z))
        #combines core numbers and border numbers dictionaries
        totalDict.update(corePairings)
        #print("totalDict: ", totalDict)
        allPairings.append(totalDict)
    """for z in itertools.permutations(corePositions):
        count = 0
        for a in z:
            newCore[a] = coreNumbers[count]
            count += 1
    for k in h4position:"""
    print("corePairings: ", corePairings)

#it looks like allcorepairings is just spitting out the same thing over and over again! Fix!!
print("These are the first few entries in allPairings: ", allPairings[1:7])

""" this will generate possible solutions, but the correct solution is not
included. Somewhere along the way, something is not being iterated through
completely/properly"""

count3 = 0
for x in allPairings:
    count3 += 1
    currentPairing = x
    if count3 < 8:
        #print("current Pairing: ", currentPairing)
        print("allPairings x: ", x)
        print("x['b']: ", x['b'])
    #print("allCorePairings[x]")
    #print(x['b'])
    if int(x['b']) + int(x['e']) + int(x['i']) + int(x['m']) == 38 and x['b'] + x['f'] +x['k'] + x['p'] == 38\
        and x['g'] + x['f'] + x['e'] + x['d'] == 38\
        and x['g'] + x['k'] + x['o'] + x['r']== 38:
        print("Possible solution: ", x)

    """if x['b'] + x['e'] + x['i'] + x['m'] == 38 and x['g'] + x['f'] + x['e'] + x['d'] == 38:
        print("Possible solution: ", x)"""



