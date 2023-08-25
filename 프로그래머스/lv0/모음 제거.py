def solution(my_string):
    replacements = {"a": "", "e": "", "i":"", "o":"","u":""}

    modified_string = "".join([replacements[char] if char in replacements else char for char in my_string])
    return modified_string