# 1. It is easy to confuse yourself and pay attention to the step size.
def solution(grid):
    def check_row(i):
        s = set()
        for j in range(9):
            if grid[i][j] >='1' and grid[i][j] <='9':
                if grid[i][j] in s:
                    return False
                s.add(grid[i][j])
        return True
    def check_col(j):
        s = set()
        for i in range(9):
            if grid[i][j] >='1' and grid[i][j] <='9':
                if grid[i][j] in s:
                    return False
                s.add(grid[i][j])
        return True
    def check_area(i, j):
        s = set()
        for di in range(3):
            for dj in range(3):
                if grid[i + di][j + dj] >='1' and grid[i + di][j + dj] <='9':
                    if grid[i + di][j + dj] in s:
                        return False
                    s.add(grid[i + di][j + dj])
        return True
    for i in range(9):
        if not check_row(i):
            return False
    for j in range(9):
        if not check_col(j):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_area(i, j):
                return False
                
    return True