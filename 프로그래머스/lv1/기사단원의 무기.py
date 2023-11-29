def solution(number, limit, power):
    divisor_cnt = 0
    answer = 0
    
    for i in range(1, number+1):
        for j in range(1,int(i**0.5)+1):
            if i % j == 0:
                divisor_cnt += 2
            if i / j == j:
                divisor_cnt -= 1
        if divisor_cnt > limit:
            answer += power
        else:
            answer += divisor_cnt
        divisor_cnt = 0
    return answer