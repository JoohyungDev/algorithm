# https://100.pyalgo.co.kr/?page=61#

from collections import deque


def solution(data):
    origin, order_list = data
    origin = deque(origin)
    for order, order_cnt in order_list:
        if order == "왼쪽":
            for _ in range(order_cnt):
                origin.popleft()
        elif order == "오른쪽":
            for _ in range(order_cnt):
                origin.pop()
    return list(origin)


solution([[1, 2, 3, 4, 5], [("왼쪽", 2), ("오른쪽", 1)]])
