# https://100.pyalgo.co.kr/?page=31#

def solution(data):
    binary = bin(data)[2:]
    # zfill은 결과값이 항상 문자열!
    binary = binary.zfill(10)
    result = binary.replace('1', '2').replace('0', '1').replace('2', '0')
    return int(result, 2)

print(solution(5))

# def solution(data):
#     binary = bin(data)[2:]
#     binary = binary.zfill(10)
#     result = ''

#     for i in binary:
#         if i == '1':
#             result += '0'
#         else:
#             result += '1'
#     return int(result, 2)