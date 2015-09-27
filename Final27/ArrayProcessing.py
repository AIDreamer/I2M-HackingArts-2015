__author__ = 'khainguyen'
# So it is 2:30 in the moring
# and I was pretty tired
# So let's see how it goes
# And I kind of forget a lot of things about Python already
#LET'S DO IT!

#Khai Nguyen

#--------***------------#

def arrayBigToSmall(aList,x,y):
    blastRadius = 79
    #get real radius
    radius = min(blastRadius,x,y,abs(len(aList)-x - 1), abs(len(aList[0]) - y - 1));
    #cut
    smallList = []

    for row in range(x-radius,x+radius+1):
        aRow = []
        for column in range(y - radius, y + radius+1):
            aRow.append(aList[column][row])
        smallList.append(aRow)
    return smallList

#work
def roundToList(smallList):
    ONE_LOOP = 20

    centerX = len(smallList)//2
    centerY = centerX
    resultList = []
    for radius in range(len(smallList)//2+1):
        aRow = []
        for x in range(centerX - radius,centerX + radius + 1):
            for y in range(centerY - radius, centerY + radius + 1):
                if (x == centerX - radius) or (x == centerX + radius) \
                        or (y == centerY - radius) or (y == centerY + radius):
                        aRow.append(smallList[x][y])
        resultList.append(aRow)
    newList = []
    counter = -1
    for x in range(len(resultList)):
        if x % ONE_LOOP == 0:
            newList.append([])
            counter += 1
        for i in resultList[x]:
            newList[counter].append(i)
    return newList

#work
#print out the array in a nice format
def niceArray(aArray):
    print()
    for i in range(len(aArray)):
        for j in range(len(aArray[i])):
            print(aArray[i][j])
        print()

def arrayAutoGenerate(numRow,numColumn):
    aRow = [0] * numRow
    newArray = [aRow] * numColumn
    return newArray



