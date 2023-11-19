def solution(s1, s2):
    mp1 = {}
    mp2 = {}
    for ch in s1:
        if ch in mp1:
            mp1[ch] += 1
        else:
            mp1[ch] = 1
    for ch in s2:
        if ch in mp2:
            mp2[ch] += 1
        else:
            mp2[ch] = 1
    ans = 0
    for k, v in mp1.items():
        if k in mp1 and k in mp2:
            ans += min(v, mp2[k])
    for k, v in mp2.items():
        if k in mp2 and k in mp1:
            ans += min(v, mp1[k])
    return ans // 2