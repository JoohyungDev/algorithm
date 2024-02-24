# https://100.pyalgo.co.kr/?page=42#

from collections import deque
def solution(data):
    size, requests = data['size'], data['requests']
    result = deque(maxlen=size) # 최대 길이 값을 넘으면 가장 오래된 값이 자동 삭제
    for i in requests:
        result.append(i)
    return list(result)

solution({'size': 3, 'requests': ['A', 'B', 'C', 'D']})