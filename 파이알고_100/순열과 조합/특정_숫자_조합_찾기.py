# https://100.pyalgo.co.kr/?page=69#


# two-pointer 알고리즘
def solution(data):
    my_list, target = data
    my_list.sort()
    result = []
    left, right = 0, len(my_list) - 1
    while left < right:
        current_sum = my_list[left] + my_list[right]
        if current_sum == target:
            pair = (my_list[left], my_list[right])
            if pair not in result:
                result.append(pair)
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return result


solution([[1, 2, 3, 4, 5], 5])

# 모듈 사용 풀이
# import itertools


# def solution(data):
#     my_list, target = data
#     nCr = itertools.combinations(my_list, 2)
#     result = []
#     for i in nCr:
#         if sum(i) == target:
#             if i not in result:
#                 result.append(i)
#     return result


# solution([[1, 2, 3, 4, 5], 5])
