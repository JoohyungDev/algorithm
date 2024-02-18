# https://100.pyalgo.co.kr/?page=37#

import re
def solution(data):
    p = r"\[(\d{2}:\d{2}:\d{2})\] (.*)"
    match = re.search(p, data) # 주어진 정규표현식(p)에 맞는 첫 번째 문자열 반환
    time = match.group(1) # 시간 추출, group(0) = 전체 문자열 
    message = match.group(2) # 메시지 추출, (.*) 부분
    return {'time':time,'message':message}

solution("[08:55:45] 사용자 로그인")