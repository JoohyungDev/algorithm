def solution(my_string):
    unique_chars = []
    [unique_chars.append(char) for char in my_string if char not in unique_chars]
    result = ''.join(unique_chars)
    return result

# def solution(my_string):
#     return ''.join(dict.fromkeys(my_string))
