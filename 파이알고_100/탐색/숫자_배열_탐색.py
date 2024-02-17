# https://100.pyalgo.co.kr/?page=21#

def solution(data):
    my_list, target = data
    if target in my_list:
        return my_list.index(target)
    return False