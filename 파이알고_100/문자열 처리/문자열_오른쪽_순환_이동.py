# https://100.pyalgo.co.kr/?page=65#

from collections import deque


def solution(data):
    text, N = data
    my_text = deque(text)
    my_text.rotate(N)
    return "".join(my_text)


solution(["abcd", 1])
