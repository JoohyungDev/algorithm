# https://100.pyalgo.co.kr/?page=44#

# from collections import Counter

# def solution(data):
#     data = data.split(',')
#     result = []
#     for i in result:
#         i = i.lower()
#         if ' ' in i:
#             result.append(i.split())
#         else:
#             result.append(i)
#     return dict(Counter(sum(result, [])))

import string
def solution(data):
    # 주어진 텍스트에서 모든 구두점을 제거하고, 소문자로 변환
    # string.punctuation : 모든 구두점 문자를 포함한 문자열
    # maketrans 함수의 첫 번째와 두 번째 파라미터는 1:1 대응되는 문자의 변환
    # 세 번째 파라미터는 제거할 문자들
    text = data.translate(str.maketrans('', '', string.punctuation)).lower()
    freq = {}
    for word in text.split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

solution("Hello world, hello")