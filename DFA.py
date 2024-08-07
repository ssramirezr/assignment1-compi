def inFinalState(finalStates, val):
    return val in finalStates

def firstComparison(finalStates, m, semiResults):
    s = 0
    x = len(m)

    for i in range(x):
        val = m[i][s]

        val1 = inFinalState(finalStates, val)

        for j in range(i + 1, x):
            val = m[j][s]
            val2 = inFinalState(finalStates, val)

            if val1 != val2:
                semiResults[j-1][i] = False

    return 0

def secondComparison(finalStates, m, semiResults):

    base = 0
    fs = len(m[0])

    while base < len(semiResults):

        for i in range(base, len(semiResults)):
            if semiResults[i][base] == True: # i = 2, base = 2 , j = 1 , v1 =  , v2 = 
                
                for j in range(1, fs):

                    value1 = m[base][j] # 
                    value2 = m[i + 1][j] # 

                    val1 = inFinalState(finalStates, value1)
                    val2 = inFinalState(finalStates, value2)
                    
                    if val1 != val2:
                        semiResults[i][base] = False
                        break

        base += 1

    return 0

def thirdComparison(finalStates, m, semiResults):

    base = 0
    fs = len(finalStates) # 3

    while base < len(semiResults):

        for i in range(base, len(semiResults)):
            if semiResults[i][base] == True:   # i = 2, base = 0, j = 1 , v1 =  , v2 = 
                
                for j in range(1, fs-1):

                    value1 = m[base][j] # 1
                    value2 = m[i + 1][j] # 5

                    if ((value2 - 1) < len(semiResults) and value1 < len(semiResults)) and (semiResults[value2-1][value1] == False):
                        semiResults[i][base] = False
                        break

                    
                    

        base += 1

    return 0

def orderedPairs(semiResults, results):

    base = 0

    while base < len(semiResults):

        for i in range(base, len(semiResults)):
            if semiResults[i][base] == True:
                
                flag = 1
                for k in results:
                    if (k[0] == base) and (k[1] == (i + 1)):
                        flag = 0
                
                if flag == 1:
                    results.append([base, (i + 1)])
        
        base += 1

    return 0


c = int(input())

for k in range(0, c):
    
    results = []
    semiResults = []

    n = int(input())

    alphabet_string = input()
    alphabet = alphabet_string.split()

    value = len(alphabet) + 1

    semiResults = [[True for _ in range(i + 1)] for i in range(n-1)]


    finalStates_string = input()
    finalStates_str = finalStates_string.split()
    finalStates = list(map(int, finalStates_str))

    m = []

    for i in range(0, n):
        row_string = input()
        row_str = row_string.split()
        row = list(map(int, row_str))
        m.append(row)
    
    firstComparison(finalStates, m, semiResults)

    secondComparison(finalStates, m, semiResults)

    thirdComparison(finalStates, m, semiResults)

    orderedPairs(semiResults, results)

    print("\n")
    for pair in results:
        print(f' ({pair[0]}, {pair[1]})', end=" ")
    print("\n")