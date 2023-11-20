def solution(roadRegister):
    n = len(roadRegister)
    In = [0 for i in range(n)]
    Out = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if roadRegister[i][j]:
                Out[i] += 1
                In[j] += 1
    for i in range(n):
        if In[i] != Out[i]:
            return False
    return True