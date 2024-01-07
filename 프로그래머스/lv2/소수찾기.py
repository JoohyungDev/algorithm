from itertools import permutations
import math

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    result_set = set()
    
    # 각 길이에 대한 순열을 구함
    for length in range(1, len(numbers) + 1):
        # 문자열의 모든 순열에 대해
        for p in permutations(numbers, length):
            # 첫 글자가 '0'인 경우 제외
            if p[0] != '0':
                # 순열을 합쳐서 숫자로 변환
                num = int(''.join(p))
                # 결과 set에 추가
                result_set.add(num)
                
    # 소수 판별 및 카운트
    return sum(is_prime(i) for i in result_set)
