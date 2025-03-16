#elementary row operations

def interchange(m: list, indexRowA: int, indexRowB: int) -> list:
    print("R{A} <-> R{B}".format(A = indexRowA + 1, B = indexRowB + 1))
    temp = m[indexRowB]
    m[indexRowB] = m[indexRowA]
    m[indexRowA] = temp
    printMatrix(m)
    print()
    return m

def multiply(m: list, indexRow: int, constMultiple: float) -> list:
    print("R{i} <- {c:.2f}R{i}".format(i = indexRow + 1, c = constMultiple))
    for i in range (len(m[indexRow])):
        m[indexRow][i] = m[indexRow][i] * constMultiple
    printMatrix(m)
    print()
    return m

def addConst(m: list, indexRowAdd: int, indexRowMult: int, constMultiple: float) -> list:
    print("R{A} <- {c:.2f}R{B} + R{A}".format(A = indexRowAdd + 1, B = indexRowMult + 1, c = constMultiple))
    for i in range (len(m[indexRowAdd])):
        m[indexRowAdd][i] = (m[indexRowMult][i] * constMultiple) + m[indexRowAdd][i]
    printMatrix(m)
    print()
    return m

#prints matrix
def printMatrix(m: list) -> list:
    for row in m:
        print("[ ", end = '')
        for i in range(0, len(row)):
            print('{:.2f}'.format(row[i]), end = ' ')
        print(']')

#Helper function for elim
#Rearranges the rows: starts from indicated row number, rows with entry 0 in the column number are sent to the bottom
def rearrangeRows(m: list, columnNumber: int, rowNumber: int) -> list:
    rowZeroes = []
    for rowNum in range(0, len(m)):
        if m[rowNum][columnNumber] == 0:
            rowZeroes.append(-1)
        else:
            rowZeroes.append(rowNum+1)

    top = rowNumber
    bottom = len(m) - 1
    while top < bottom:
        if rowZeroes[top] == -1:
            while rowZeroes[bottom] == -1:
                bottom -= 1
            if bottom < top:
                break
            m = interchange(m, top, bottom)
            tempIndex = rowZeroes[top]
            rowZeroes[top] = rowZeroes[bottom]
            rowZeroes[bottom] = tempIndex
        else:
            top += 1
    return m

#performs Gaussian elimination on an augmented matrix; returns a matrix in row echelon form
def elim(m: list):
    for i in range(0, len(m)):
        m = rearrangeRows(m, i, i)
        if m[i][i] != 0 and m[i][i] != 1:
            m = multiply(m, i, 1/(m[i][i]))
        for j in range(i+1, len(m)):
            if -m[j][i] != 0:
                m = addConst(m, j, i, -m[j][i])
    return m

#converts a matrix in row-echelon form into row-reduced echelon form
def rref(m: list):
    lastIndex = len(m) - 1
    for i in range(0, len(m)-1):
        for j in range(0, len(m[lastIndex - i])):
            if m[lastIndex - i][j] == 1:
                indexOf1 = j
                break
            if m[lastIndex - i][j] != 1 and j == len(m[lastIndex - i])-1:
                indexOf1 = -1
        if indexOf1 == -1:
            continue
        else:
            for k in range(0, lastIndex-i):
                addConst(m, k, lastIndex-i, -m[k][indexOf1] )
    return m

#sample output
#each entry of matrix is a row. the size of matrix corresponds to the number of columns
matrix = [ 
    [2, -1, 3, 4, 9], 
    [1, 0, -2, 7, 11], 
    [3, -3, 1, 5, 8], 
    [2, 1, 4, 4, 10] ] #insert your matrix here
print("Original Augmented Matrix:")
printMatrix(matrix)
print()
matrix = elim(matrix)
print("Row-echelon Form: ")
printMatrix(matrix)
print("Gauss-Jordan reduction: ")
matrix = rref(matrix)
print("Reduced-row echelon form: ")
printMatrix(matrix)