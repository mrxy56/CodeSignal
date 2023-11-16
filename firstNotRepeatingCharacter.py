def solution(s):
    mp = {}
    for ch in s:
        if ch in mp:
            mp[ch] += 1
        else:
            mp[ch] = 1
    for ch in s:
        if mp[ch] == 1:
            return ch
    return '_'

