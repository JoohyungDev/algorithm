# https://100.pyalgo.co.kr/?page=74#


def solution(data):
    str1, str2 = data
    str1, str2 = set(str1), set(str2)
    return sorted(list((str1 - str2) | (str2 - str1)))


solution(["apple", "peer"])
