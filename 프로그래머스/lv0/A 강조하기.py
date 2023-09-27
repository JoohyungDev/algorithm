def solution(myString):
    modified_string = ''.join([s.upper() if s == 'a' or s == 'A' else s.lower() for s in myString])
    return modified_string