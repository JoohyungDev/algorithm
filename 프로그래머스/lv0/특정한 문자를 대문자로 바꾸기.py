def solution(my_string, alp):
    modified_string = ""
    
    for char in my_string:
        if char == alp:
            modified_string += char.upper()
        else:
            modified_string += char
    
    return modified_string

# def solution(my_string, alp):
#     return my_string.replace(alp, alp.upper())