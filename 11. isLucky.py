# 1. Cannot use half == cnt // 2 because cnt is not necessarily even.
def solution(n):
    tmp = n
    cnt = 0
    digit = 0
    while n:
        cnt += n % 10
        n = n // 10
        digit += 1
    half = 0
    for i in range(digit // 2):
        half += tmp % 10
        tmp = tmp // 10
    if half * 2 == cnt:
        return True
    return False