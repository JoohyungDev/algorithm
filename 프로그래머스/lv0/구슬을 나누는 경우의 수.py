import math

def solution(balls, share):
    return math.factorial(balls)/(math.factorial(balls-share)*math.factorial(share))

# 조합을 사용한 간단한 식
import math

def solution(balls, share):
    return math.comb(balls, share)
