def solution(num_list):
    answer = 0
    if len(num_list) > 10:
        answer = sum(num_list)
    else:
        for i in range(len(num_list)):
            if i == 0:
                init = num_list[0]
                answer += init
            else:
                answer *= num_list[i]
    return answer

# def solution(num_list):
#     if len(num_list) >= 11:
#         return eval('+'.join(list(map(str, num_list))))
#     else:
#         return eval('*'.join(list(map(str, num_list))))

# from math import prod
# def solution(num_list):
#     return sum(num_list) if len(num_list)>=11 else prod(num_list)