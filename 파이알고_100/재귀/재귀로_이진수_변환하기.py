# https://100.pyalgo.co.kr/?page=97#


def solution(n):
    if n == 0:
        return "0"

    def helper(n):
        if n == 0:
            return ""
        else:
            return helper(n // 2) + str(n % 2)

    result = helper(n)
    return result if result != "" else "0"
