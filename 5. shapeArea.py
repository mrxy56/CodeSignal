# 1. Do not calculate the formula first, instead, find the patterns.
def solution(n):
    ans = 0
    ans += (n - 1) * 2 + 1
    n = n - 1
    while n > 0:
        ans += ((n - 1) * 2 + 1) * 2
        n = n - 1
    return ans
    
