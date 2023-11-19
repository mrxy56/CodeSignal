def solution(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(1, n):
        for j in range(m):
            if matrix[i - 1][j] == 0:
                matrix[i][j] = 0
    ans = 0
    for i in range(n):
        for j in range(m):
            ans += matrix[i][j]
    return ans

