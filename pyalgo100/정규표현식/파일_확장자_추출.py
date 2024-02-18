# https://100.pyalgo.co.kr/?page=39#

def solution(data):
    my_str = data.split('.')
    return my_str[-1] if len(my_str) != 1 else ''

solution("example/document.pdf")

# def get_file_extension(path_or_url):
#     # 파일명에서 마지막 점의 위치를 찾는다.
#     dot_index = path_or_url.rfind('.')
    
#     # 마지막 점이 없다면, 파일 확장자가 없는 것이므로 빈 문자열을 반환한다.
#     if dot_index == -1:
#         return ''
        
#     # 마지막 점 이후의 문자열을 확장자로 반환한다.
#     return path_or_url[dot_index+1:]

# import re

# def get_file_extension(path_or_url):
#     # 마지막 점 이후의 모든 문자를 찾는 정규 표현식 패턴
#     pattern = r'\.([a-zA-Z0-9]+)$'
    
#     # 정규 표현식으로 검색하고, 일치하는 부분을 찾는다.
#     match = re.search(pattern, path_or_url)
    
#     # 일치하는 부분이 있다면, 그 값을 반환하고, 없다면 빈 문자열을 반환한다.
#     return match.group(1) if match else ''