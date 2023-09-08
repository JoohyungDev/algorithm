def solution(my_string, m, c):
    init = 0
    answer = ''
    target_string = ''
    i = 1
    
    if m == 1:
        return my_string
    
    for i in range(len(my_string)):
        if i % m == 0:
            init = i
            target_string = my_string[init:init+m]
            answer += target_string[c-1]
    return answer
            
# def solution(s, m, c):
#     return s[c-1::m]