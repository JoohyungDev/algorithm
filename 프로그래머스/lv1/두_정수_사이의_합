def solution(a, b):
    sum = 0
    if a < b:
        for i in range(a + 1, b):
            sum = sum + i
    if a > b:
        for i in range(b+1, a):
            sum = sum + i
    sum = sum + a + b             
    if a == b:
        sum = a  
    return sum

print(solution(1, 3))

# return (abs(a-b)+1)*(a+b)//2 이런 코드도 가능하다
# sum(range(min(a,b),max(a,b)+1)) 최소 ~ 최대 값까지 더하는 코드        