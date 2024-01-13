# https://100.pyalgo.co.kr/?page=8#

def solution(data):
    x = list(zip(data, data[1:]))   
    return list(sorted(x, key=lambda x: x[1] - x[0])[0])
