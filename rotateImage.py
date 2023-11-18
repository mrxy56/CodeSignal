# 1. Rotate any elements, only four of them are affected.
# 2. Only rotate the upper left, pay attention to odd or even row numbers.
# 3. Map should be calculated by drawing the picture.
def solution(a):
    n = len(a)
    m = len(a[0])
    r = n
    c = m
    if n % 2 == 0:
        r = n // 2
        c = m // 2
    if n % 2 == 1:
        r = n // 2 + 1
        c = m // 2
    for i in range(r):
        for j in range(c):
            tmp = a[i][j]
            a[i][j] = a[n - 1 - j][i]
            a[n - 1 - j][i] = a[n - 1 - i][n - 1 - j]
            a[n - 1 - i][n - 1 - j] = a[j][n - 1 - i]
            a[j][n - 1 - i] = tmp
    return a
