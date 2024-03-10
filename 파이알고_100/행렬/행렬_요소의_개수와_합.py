# https://100.pyalgo.co.kr/?page=59#

# 효율적인 반복을 위한 도구를 제공
import itertools


def solution(data):
    matrix, target = data
    cnt, total = 0, 0
    # itertools.chain.from_iterable는 이터레이터를 반환함
    # 이터레이터 = 반복 가능한 객체
    flattened = itertools.chain.from_iterable(matrix)
    # print(list(flattened)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in flattened:
        if i >= target:
            cnt += 1
            total += i
    return (cnt, total)


solution([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5])
