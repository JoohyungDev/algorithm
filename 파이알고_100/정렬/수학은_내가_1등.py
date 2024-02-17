# https://100.pyalgo.co.kr/?page=9#

def solution(data):
    result = sorted(data, key=lambda x:x['수'], reverse=True)
    return result[0]['이름']