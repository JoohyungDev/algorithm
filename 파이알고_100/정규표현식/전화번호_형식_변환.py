# https://100.pyalgo.co.kr/?page=36#

import re
def solution(data):
    p = re.sub(r'(\d{3})(\d{4})(\d{4})', r'\1-\2-\3', data)
    return p

solution("항상 여기로 연락주세요 01012345678.")