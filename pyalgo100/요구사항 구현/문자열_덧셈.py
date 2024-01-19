# https://100.pyalgo.co.kr/?page=6#

# def solution(data):
#     return sum(int(i) for i in data if i.isdigit())

def solution(data):
    import re
    
    digit_list = re.findall(r'[0-9]', data)
    return sum(map(int,digit_list))