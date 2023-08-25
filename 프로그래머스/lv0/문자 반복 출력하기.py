def solution(my_string, n):
    answer = ""
    for str in my_string:
        answer += str*(n)
    return answer

# def solution(my_string, n):
#     return ''.join(i*n for i in my_string)