# https://100.pyalgo.co.kr/?page=71#


def solution(data):
    new_list = list(dict.fromkeys(data))
    return "".join(new_list)


solution("banana")

# def solution(data):
#     result = ''
#     for i in data:
#         if i not in result:
#             result += i
#     return result
