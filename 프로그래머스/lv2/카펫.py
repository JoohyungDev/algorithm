import math

def solution(brown, yellow):
    total = brown + yellow
    
    for i in range(1, int(math.sqrt(total)) + 1):
        if total % i == 0:
            j = total // i
            if (i-2) * (j-2) == yellow:
                return [max(i, j), min(i, j)]

# https://school.programmers.co.kr/questions/52491 참고해볼 만한 글