# https://100.pyalgo.co.kr/?page=2#

def solution(data):
    result = 1
    
    if len(data) == 0:
        return 0
    
    for i in data:
        result *= i
    return result