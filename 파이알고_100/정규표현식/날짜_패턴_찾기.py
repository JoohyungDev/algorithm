# https://100.pyalgo.co.kr/?page=34#
import re

def solution(data):
    p = re.findall(r'[0-9]+-[0-9]+-[0-9]+', data)
    return [tuple(map(int, i.split('-'))) for i in p]

solution("Dates: 2023-12-31, 2024-01-01, and 2024-02-28.")