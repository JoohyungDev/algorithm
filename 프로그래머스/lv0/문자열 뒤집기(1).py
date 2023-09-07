def solution(my_string, s, e):
    reverse_string = my_string[s:e+1]
    return my_string[:s]+reverse_string[::-1]+my_string[e+1:]
