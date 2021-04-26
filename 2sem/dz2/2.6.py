def transpose(matrix):
    matrix2 = []
    N = len(matrix)
    M = len(matrix[0])
    for i in range(M):
        matrix1 = []
        for j in range(N):
            matrix1.append(matrix[j][i])
        matrix2.append(matrix1)
    matrix[:] = matrix2[:]


matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)