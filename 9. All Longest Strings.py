def solution(inputArray):
    cnt = 0
    for w in inputArray:
        if len(w) > cnt:
            cnt = len(w)
    ret = []
    for w in inputArray:
        if len(w) == cnt:
            ret.append(w)
    return ret
