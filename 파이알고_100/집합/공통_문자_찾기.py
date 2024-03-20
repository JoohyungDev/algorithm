# https://100.pyalgo.co.kr/?page=72#


def solution(data):
    str1, str2 = data
    set1 = set(str1)
    set2 = set(str2)
    return sorted(list(set1 & set2))
