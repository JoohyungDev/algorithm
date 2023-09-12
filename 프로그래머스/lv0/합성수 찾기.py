def solution(n):
    output = 0
    for i in range(4, n + 1):
        # 대부분 자연수의 약수는 대상의 제곱근 이하의 약수 하나와 이상의 약수 하나씩 한 쌍을 이룸(j)
        for j in range(2, int(i ** 0.5) + 1): 
            if i % j == 0:
                output += 1
                break
    return output
