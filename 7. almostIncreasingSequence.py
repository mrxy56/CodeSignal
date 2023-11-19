# 1. Cannot use greedy. Find the break point and test it.
# 2. Edge case is the break point is at the first or last.
def solution(sequence):
    n = len(sequence)
    if n == 2:
        return True
    l = 0
    r = n - 1
    while (l < r and sequence[l] < sequence[l + 1]):
        l += 1
    while (l < r and sequence[r - 1] < sequence[r]):
        r -= 1
    if l + 1 == r:
        if sequence[l] < sequence[r]:
            return True
        if l == 0 or l > 0 and sequence[l - 1] < sequence[r]:
            return True
        if r == n - 1 or r < n - 1 and sequence[l] < sequence[r + 1]:
            return True
    return False