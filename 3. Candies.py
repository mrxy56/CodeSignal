def solution(n, m):
    if m >= n:
        return m - m % n
    return 0
