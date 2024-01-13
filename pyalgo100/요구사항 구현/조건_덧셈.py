# https://100.pyalgo.co.kr/?page=3#

def solution(data):
    result = 0
    
    if len(data) == 0:
        return 0
    
    for i in data:
        if i % 3 != 0 and i % 5 != 0:
            result += i
    return result