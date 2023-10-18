def solution(my_string, num1, num2):
    result = ""

    for idx,i in enumerate(my_string):
        result += i
        
        if idx == num1:
            result = result[:-1]
            result += my_string[num2]

        elif idx == num2:
            result = result[:-1]
            result += my_string[num1]
            
    return result

# def solution(my_string, num1, num2):
#     s = list(my_string)
#     s[num1],s[num2] = s[num2],s[num1]
#     return ''.join(s)