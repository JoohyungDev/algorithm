# https://100.pyalgo.co.kr/?page=78#

from collections import Counter


def solution(data):
    result = Counter()
    for i in data:
        # 주어진 범위의 모든 숫자를 생성하고 개수를 센 후
        # result에 넘겨준다.
        result.update(range(i[0], i[1]))
    return len([item for item in result.items() if item[1] >= 2])


solution([[1, 5], [3, 7], [2, 6]])
