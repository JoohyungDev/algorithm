# https://100.pyalgo.co.kr/?page=45#

from collections import deque

def solution(data):
    queue1, queue2 = deque(data['queue1']), deque(data['queue2'])
    sum1, sum2 = sum(queue1), sum(queue2)
    len1, len2 = len(queue1), len(queue2)
    target = (sum1 + sum2) // 2
    cnt = 0
    for _ in range(len1+len2):
        cnt += 1
        if sum1 > target:
            moved = queue1.popleft()
            queue2.append(moved)
            sum1 -= moved
            sum2 += moved
        elif sum1 < target:
            moved = queue2.popleft()
            queue1.append(moved)
            sum1 += moved
            sum2 -= moved
        if sum1 == target:
            return cnt
    return -1

solution({'queue1': [1, 2, 1, 2], 'queue2': [1, 10, 1, 2]} )