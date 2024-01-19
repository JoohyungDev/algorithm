# https://100.pyalgo.co.kr/?page=14#

def solution(data):
    result = []
    codes = sorted(data.items(), key=lambda x:x[0])
    
    for code,name in codes:
        result.append(name)
    return result

