# https://100.pyalgo.co.kr/?page=23#

def solution(data):
    my_list, target = data
    my_list = sum(my_list, [])
    if target in my_list:
        return True
    return False