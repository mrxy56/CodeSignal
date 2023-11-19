def solution(divisor, bound):
    for i in range(bound, divisor - 1, -1):
        if i % divisor == 0:
            return i
            

