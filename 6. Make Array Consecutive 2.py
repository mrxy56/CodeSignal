def solution(statues):
    mini = min(statues)
    maxi = max(statues)
    return maxi - mini + 1 - len(statues)
