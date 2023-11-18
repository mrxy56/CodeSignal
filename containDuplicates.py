def solution(a):
    s = set()
    for e in a:
        if e in s:
            return True
        s.add(e)
    return False

