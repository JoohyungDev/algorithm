def solution(n):
    # n을 2로 나눴을때 몫만큼 2의 배수를 더한다
    quotient = n // 2
    sum = 0
    for i in range(quotient+1):
        sum += (2*i)
    return sum