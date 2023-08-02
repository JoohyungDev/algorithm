def solution(n):
    data = []
    if n == 0:
        data.append(0)
    if n != 0:
        for i in range(1, n+1):
            divisor = n % i
            if divisor == 0:
                data.append(i)
    print("{0}의 약수는 {1}입니다. 이를 모두 더하면 {2}입니다.".format(n, data, sum(data) ))

solution(0)

# return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])으로 간단하게 끝내기도 가능하다.
# 