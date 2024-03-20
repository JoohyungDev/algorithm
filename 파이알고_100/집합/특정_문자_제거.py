# https://100.pyalgo.co.kr/?page=73#


def solution(data):
    str1, str2 = data
    str1 = set(str1)
    str2 = set(str2)
    return sorted(list(str1 - str2))


solution(["apple", "ple"])
