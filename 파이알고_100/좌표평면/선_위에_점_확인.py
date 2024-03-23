# https://100.pyalgo.co.kr/?page=77#


def solution(data):
    my_list, target = data
    return target in range(my_list[0], my_list[1] + 1)


solution([[1, 5], 3])
