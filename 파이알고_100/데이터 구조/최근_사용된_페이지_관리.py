# https://100.pyalgo.co.kr/?page=43#

from collections import deque
def solution(data):
    size, pages = data['size'], data['pages']
    result = deque(maxlen=size)
    for i in pages:
        if not i in result:
            result.append(i)
        else:
            result.remove(i)
            result.append(i)
    return list(result)