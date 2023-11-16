def solution(a):
    n = len(a)
    d = [0 for i in range(n + 1)]
    d[0] = 1
    for e in a:
        if d[e] == 1:
            return e
        d[e] = 1
    return -1