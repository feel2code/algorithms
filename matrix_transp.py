def matrix_transp(rows, cols, matrix):
    transp = []
    for col in range(0, cols):
        for row in range(0, rows):
            transp.append(matrix[row][col])
    i = 0
    for col in range(i, cols):
        print(' '.join(map(str, transp[i:(i + rows)])))
        i += rows

if __name__ == "__main__":
    rows = int(input())
    cols = int(input())
    matrix = []
    for row in range(0, rows):
        matrix.append(list(map(str, input().split())))
    matrix_transp(rows, cols, matrix)
