# https://100.pyalgo.co.kr/?page=62#

from collections import deque


def solution(data):
    target, my_list = data
    my_q = deque(maxlen=target)
    result = []
    for i in my_list:
        my_q.append(i)
        result.append(list(my_q))
    return result


solution([3, [1, 2, 3, 4, 5]])
