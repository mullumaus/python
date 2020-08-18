import  numpy as np

def matrix(n):
    result = np.zeros(shape=(n,n))

    counter = 1
    startColumn = 0
    endColumn = n -1
    startRow = 0
    endRow = n -1
    while(startColumn <= endColumn and startRow <=endRow):
        for i in range(startColumn,endColumn+1):
            result[startRow][i] =counter
            counter = counter + 1
        startRow = startRow + 1
        for i in range(startRow,endRow+1):
            result[i][endColumn] = counter
            counter = counter + 1
        endColumn = endColumn - 1
        for i in range(endColumn,startColumn-1,-1):
            result[endRow][i] = counter
            counter = counter + 1
        endRow = endRow - 1
        for i in range(endRow,startRow-1, -1):
            result[i][startColumn] = counter
            counter = counter + 1
        startColumn = startColumn +1
    print(result)



if __name__ == "__main__":
    matrix(20)
