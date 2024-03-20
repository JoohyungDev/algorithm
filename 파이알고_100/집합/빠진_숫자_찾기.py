# https://100.pyalgo.co.kr/?page=75#


def solution(data):
    my_set, n, m = set(data[0]), data[1], data[2]
    result = [i for i in range(n, m + 1) if i not in my_set]
    return result


solution([[2, 3, 4], 1, 5])

# def solution(data):
#     my_list, n, m = data
#     result = []
#     for i in range(n,m+1):
#         if i not in my_list:
#             result.append(i)
#     return result
