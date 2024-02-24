# https://100.pyalgo.co.kr/?page=38#

import re

def solution(url):
    # *표시는 가능한 많은 패턴을 찾기에 *와 ?를 같이 사용해 첫번째 패턴을 찾으면 종료하도록 설정
    pattern = re.compile(r'(.*?):\/\/([^\/]*)(\/[^?]*)?(\?.*)?')
    match = pattern.search(url)
    
    if match is None:
        return {'protocol': '', 'domain': '', 'path': '', 'query': ''}
    
    protocol = match.group(1) if match.group(1) else ''
    domain = match.group(2) if match.group(2) else ''
    path = match.group(3) if match.group(3) else ''
    query = match.group(4)[1:] if match.group(4) else ''
    
    return {'protocol': protocol, 'domain': domain, 'path': path, 'query': query}

solution("https://www.weniv.co.kr/path/to/resource?user=abc&lang=en")