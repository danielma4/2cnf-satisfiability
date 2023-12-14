#function which places implication graph into adjacency list
def placeData(p, q):
    posIndexP = (2 * abs(p)) - 2
    posIndexQ = (2 * abs(q)) - 2
    negIndexP = (2 * abs(p)) - 1
    negIndexQ = (2 * abs(q)) - 1
    if firstNum > 0 and secondNum > 0:
        graph[negIndexP].append(posIndexQ)
        graph[negIndexQ].append(posIndexP)
    elif firstNum > 0 and secondNum < 0:
        graph[negIndexP].append(negIndexQ)
        graph[posIndexQ].append(posIndexP)
    elif firstNum < 0 and secondNum > 0:
        graph[posIndexP].append(posIndexQ)
        graph[negIndexQ].append(negIndexP)
    else:
        graph[posIndexP].append(negIndexQ)
        graph[posIndexQ].append(negIndexP)

#DFS which fills a path queue
vis = [] 
def fillPath(startRow):
    if (startRow in vis):
        return
    vis.append(startRow)
    for c in range(len(graph[startRow])):
        if (graph[startRow][c] not in vis) :
            pathQ.append(graph[startRow][c])
        else:
            continue
        fillPath(graph[startRow][c]) 

#assigns variables if no contradictions found
imp = 0
def assignVariables(ogList, i, pathQ): 
    dummyAssignments = [0 for i in range(2 * variableCount)]

    for x in range(len(dummyAssignments)):
        dummyAssignments[x] = ogList[x]

    if (i % 2 == 0):
        if (dummyAssignments[i] == -1 or dummyAssignments[i + 1] == 1):
            return ogList
        else:
            dummyAssignments[i] = 1
            dummyAssignments[i + 1] = -1
    else:
        if (dummyAssignments[i] == -1 or dummyAssignments[i - 1] == 1):
            return ogList
        else:
            dummyAssignments[i] = 1
            dummyAssignments[i - 1] = -1

    for u in range(len(pathQ)):
        imp = pathQ.pop(0)
        if (imp % 2 == 0):
            if (dummyAssignments[imp] == -1 or dummyAssignments[imp + 1] == 1):
                return ogList
            else:
                dummyAssignments[imp] = 1
                dummyAssignments[imp + 1] = -1
        else:
            if (dummyAssignments[imp] == -1 or dummyAssignments[imp - 1] == 1):
                return ogList
            else:
                dummyAssignments[imp] = 1
                dummyAssignments[imp - 1] = -1

    return dummyAssignments

#mapping function
def intToVariable(index):
    if (index % 2 == 0):
        return int((index + 2) / 2)
    else:
        return int(-((index + 1) / 2))

variableCount = 0
#first pass -- count variables
with open("test8.txt") as fileIn:
    for line in fileIn:
        firstNum, secondNum = [int(s) for s in line.split()]
        highestNum = max(abs(firstNum), abs(secondNum))
        if highestNum > variableCount:
            variableCount = highestNum

#initialize adjacency list with 2n lists
graph = [list() for i in range (2 * variableCount)]

#positive numbers: i = 2v - 2
#negative numbers: i = 2v - 1
#2nd pass -- traverse data and place into list
with open("test8.txt") as fileIn:
    firstZero = 0
    secondZero = 0
    for line in fileIn:
        firstNum, secondNum = [int(s) for s in line.split()]
        placeData(firstNum, secondNum)

print("Adjacency List:")
for i in range(len(graph)):
    print(graph[i])

pathQ = list()
assignments = [0 for i in range(2 * variableCount)]

for i in range(len(assignments)):
    pathQ.clear()
    vis.clear()
    fillPath(i)
    assignments = assignVariables(assignments, i, pathQ)

if 0 in assignments:
    print("NO SATISFACTORY ASSIGNMENT") 
else:
    print("Assignments: ")
    for i in range(len(assignments)):
        print(intToVariable(i), assignments[i], sep =": ")
