def solution(inputArray):
    n = len(inputArray)
    ans = - 10 ** 6
    for i in range(n - 1):
        if inputArray[i] * inputArray[i + 1] > ans:
            ans = inputArray[i] * inputArray[i + 1]
    return ans
