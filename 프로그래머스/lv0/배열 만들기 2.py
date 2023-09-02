def solution(l, r):
    result = []
    for i in range(l,r+1):
        if all(digit in '50' for digit in str(i)):
            result.append(i)
    if len(result) == 0:
        result.append(-1)
    return result

# def solution(l, r):
#     answer = []
#     for num in range(l, r + 1):
#         if not set(str(num)) - set(['0', '5']):
#             answer.append(num)
#     return answer if answer else [-1]