import math

def solution(n):
    answer = 0
    i = 1
    while True:
        if math.factorial(i) > n:
            answer = i-1
            break
        i += 1
    return answer
