def solution(n, m):
    max = []
    for i in range(1, n+1):
        if n % i == 0:
            max.append(i)
    for j in range(1, m+1):
        if m % j == 0:
            max.append(j)
    max.sort()
    for k in max:
        if n % k == 0 and m % k == 0:
            max_result = k             # 최대공약수
    min_result = (n * m) // max_result  # 최소공배수 = 주어진 숫자의 곱 / 최대공약수
    return max_result, min_result

# def gcdlcm(a, b):
#     c, d = max(a, b), min(a, b)
#     t = 1
#     while t > 0:
#         t = c % d
#         c, d = d, t
#     answer = [c, int(a*b/c)]
#     return answer

# 유클리드 호제법으로 푼 예시이다. 유클리드 호제법은 소인수 분해 등을 하지 않고 최대공약수를 구할 수 있는 방법
# 수가 커지면 이 방법이 효율적일듯 하다 
# GCD(A,B)가 A와 B의 최대공약수라고 할 때, 둘중에서 큰수 - 작은수와 작은수의 최대공약수와 A와 B의 최대공약수는 같다. 
# 이를 반복하면 작은 수와 작은 수의 비교가 되는데 금방 최대 공약수를 구할 수 있다
# https://blog.naver.com/seekhim/222848108459 참고

# def solution(n, m):
#     gcd = lambda a,b : b if not a%b else gcd(b, a%b)
#     lcm = lambda a,b : a*b//gcd(a,b)
#     return [gcd(n, m), lcm(n, m)]
# 정수론 풀이
# lamda는 def으로 이루어진 함수 선언을 보다 간편하게 할 수 있다
# 함수명 = lamda 매개변수 : 함수내용