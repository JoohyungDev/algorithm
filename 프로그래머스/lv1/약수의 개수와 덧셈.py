def solution(left, right):
    divisor_total = 0
    answer = 0  # 최종 합
    
    for i in range(left,right+1):
        for j in range(1,i+1):
            if i%j == 0:
                divisor_total += 1
        if divisor_total % 2 == 0:
            answer += i
            divisor_total = 0
        else:
            answer -= i
            divisor_total = 0
    return answer

# 제곱수의 약수의 개수는 홀수개이다.
# 
# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer
