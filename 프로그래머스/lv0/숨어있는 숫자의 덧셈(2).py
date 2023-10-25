import re

def solution(my_string):
    return sum([int(num) for num in re.findall(r'\d+', my_string)])

# def solution(my_string):
#     s = ''.join(i if i.isdigit() else ' ' for i in my_string)
#     return sum(int(i) for i in s.split())