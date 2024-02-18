# https://100.pyalgo.co.kr/?page=40#

import re

def solution(data):
    numbers = re.findall(r'[\d,]+', data)
    result = ''.join(num.replace(',', '') for num in numbers)
    return result