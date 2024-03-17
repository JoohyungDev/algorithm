# https://100.pyalgo.co.kr/?page=70#

import itertools


def solution(data):
    my_list, _min, _max = data
    cnt = 0
    for i in range(len(my_list)):
        nCr = itertools.combinations(my_list, i + 1)
        for j in nCr:
            if _min <= sum(j) <= _max:
                cnt += 1
    return cnt


solution([[1, 2, 3, 4, 5], 5, 10])
