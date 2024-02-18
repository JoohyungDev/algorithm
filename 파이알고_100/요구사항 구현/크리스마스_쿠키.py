# https://100.pyalgo.co.kr/?page=4#

def solution(data):
    result = 0
    
    for idx, i in enumerate(data, 1):
        result += idx * int(i.split()[1][0])
    return result