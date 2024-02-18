# https://100.pyalgo.co.kr/?page=1#

# def solution(data):
#     return sum(x for x in data if x % 2 != 0)

def solution(data):
    return sum(filter(lambda x: x%2 != 0, data))