def solution(num):
    count = 0
    if num == 1: 
        return 0
    while True:
        if num % 2 == 0:
            num = num / 2
            count = count + 1 
            if num == 1:
                break
        if num % 2 != 0:
            num = num * 3 + 1
            count = count + 1
            if num == 1:
                break
        if count >= 500:
            return -1
    return count
print(solution(626331))

# for i in range(500):
#         num = num / 2 if num % 2 == 0 else num*3 + 1
#         if num == 1:
#             return i + 1
#     return -1
# 이런식으로 짧게도 가능하다. 500번 이상 돌리면 -1이므로 반복문을 500번 돌린다. 