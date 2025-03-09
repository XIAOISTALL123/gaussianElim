#elementary row operations

def interchange(m: list, indexRowA: int, indexRowB: int) -> list:
    print("R{A} <-> R{B}".format(A = indexRowA, B = indexRowB))
    temp = m[indexRowB - 1]
    m[indexRowB - 1] = m[indexRowA - 1]
    m[indexRowA - 1] = temp
    printMatrix(m)
    print()
    return m

def multiply(m: list, indexRow: int, constMultiple: float) -> list:
    print("R{i} <- {c:.2f}R{i}".format(i = indexRow, c = constMultiple))
    for i in range (len(m[indexRow-1])):
        m[indexRow-1][i] = m[indexRow-1][i] * constMultiple
    printMatrix(m)
    print()
    return m

def addConst(m: list, indexRowAdd: int, indexRowMult: int, constMultiple: float) -> list:
    print("R{A} <- {c:.2f}R{B} + R{A}".format(A = indexRowAdd, B = indexRowMult, c = constMultiple))
    for i in range (len(m[indexRowAdd-1])):
        m[indexRowAdd-1][i] = (m[indexRowMult-1][i] * constMultiple) + m[indexRowAdd-1][i]
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
    columnNumber = columnNumber - 1
    rowZeroes = []
    for rowNum in range(0, len(m)):
        if m[rowNum][columnNumber] == 0:
            rowZeroes.append(-1)
        else:
            rowZeroes.append(rowNum+1)

    top = rowNumber-1
    bottom = len(m) - 1
    while top < bottom:
        if rowZeroes[top] == -1:
            while rowZeroes[bottom] == -1:
                bottom -= 1
            if bottom < top:
                break
            m = interchange(m, top+1, bottom+1)
            tempIndex = rowZeroes[top]
            rowZeroes[top] = rowZeroes[bottom]
            rowZeroes[bottom] = tempIndex
        else:
            top += 1
    return m

#performs Gaussian elimination on an augmented matrix; returns a matrix in row echelon form
def elim(m: list):
    for i in range(1, len(m)+1):
        m = rearrangeRows(m, i, i)
        if m[i-1][i-1] != 0 and m[i-1][i-1] != 1:
            m = multiply(m, i, 1/(m[i-1][i-1]))
        for j in range(i+1, len(m)+1):
            if -m[j-1][i-1] != 0:
                m = addConst(m, j, i, -m[j-1][i-1])
    return m

#sample output
#each entry of matrix is a row. the size of matrix corresponds to the number of columns
matrix = [ [0, 1, -1, -2, -3], [1, 2, -1, 0, 2], [2, 4, 1, -3, -2], [1, -4, -7, -1, 19] ]
print("Original Augmented Matrix:")
printMatrix(matrix)
print()
matrix = elim(matrix)
print("Row-echelon Form: ")
printMatrix(matrix)