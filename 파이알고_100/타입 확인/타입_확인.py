# https://100.pyalgo.co.kr/?page=20#

def solution(data):
    for i,j in data:
        if i != type(j).__name__:
            return False
    return True