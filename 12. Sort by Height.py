# 1. It is actually easy. Just put all the non negative numbers in a new list and sort, then put them back.
def solution(a):
    ls = []
    for i, e in enumerate(a):
        if e != -1:
            ls.append(e)
    ls.sort()
    p = 0
    for i, e in enumerate(a):
        if a[i] != -1:
            a[i] = ls[p]
            p += 1
    return a
            