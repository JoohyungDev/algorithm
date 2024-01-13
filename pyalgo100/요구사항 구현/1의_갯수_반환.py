# https://100.pyalgo.co.kr/?page=5#

def solution(data):
    count = 0
    
    for i in data:
        count += str(i).count('1')
    return count