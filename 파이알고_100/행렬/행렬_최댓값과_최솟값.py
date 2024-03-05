# https://100.pyalgo.co.kr/?page=60#

import itertools


def solution(data):
    matrix, _range = data
    min_value, max_value = _range
    real_min, real_max = None, None  # 반환할 진짜 최소, 최대값
    # 범위에 해당하는 원소만 선택
    flattened = [
        i for i in itertools.chain.from_iterable(matrix) if min_value <= i <= max_value
    ]
    if flattened:
        real_min, real_max = min(flattened), max(flattened)
    return (real_max, real_min)


solution([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], (3, 7)])
