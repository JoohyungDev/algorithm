# https://100.pyalgo.co.kr/?page=11#

def solution(data):
    filtered_data = list(filter(lambda x:(x[0]+x[1]+x[2])/3>=80, data))
    return len(filtered_data)