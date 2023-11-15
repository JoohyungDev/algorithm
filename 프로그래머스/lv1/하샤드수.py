def solution(x):
    # answer = True
    # num5 = int(x/10000)
    # num4 = int((x%10000)/1000)
    # num3 = int((x%1000)/100)
    # num2 = int((x%100)/10)
    # num1 = int(x%10)
    # sum = num5+num4+num3+num2+num1
    # if x % sum != 0:
    #     answer = False
    # return answer
    return x % sum([int(c) for c in str(x)]) == 0    # sum = 배열 안의 값을 다 더함. 계산했을 때 나머지가 0이면 true.

print(solution(11))