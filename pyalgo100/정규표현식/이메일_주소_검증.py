import re
def solution(data):
    p = re.compile('[0-9a-zA-Z._+]+@[0-9a-zA-Z-.]+\.[a-zA-z]{2,}')
    result = p.match(data)
    return True if result else False
    
solution('user@example.com')