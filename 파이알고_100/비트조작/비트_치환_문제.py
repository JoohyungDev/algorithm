# https://100.pyalgo.co.kr/?page=30#

# def solution(data):
#     binary = bin(data)[2:]
#     result = ''
#     for i in str(binary):
#         if i == str(1):
#             result += 'A'
#         else:
#             result += 'B'
#     return result

def solution(data):
    binary = bin(data)[2:]
    result = binary.replace('1', 'A').replace('0', 'B')
    return result