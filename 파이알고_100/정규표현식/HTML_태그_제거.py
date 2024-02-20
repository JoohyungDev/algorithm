# https://100.pyalgo.co.kr/?page=35#

import re

def solution(data):
    p = re.sub(r'<.*?>', '', data)
    return p