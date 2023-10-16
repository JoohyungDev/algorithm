def solution(myString):
    result = ""
    
    for i in myString:
        if ord(i) < 108:
            result += "l"
        else:
            result += i
    return result

# def solution(myString):
#     return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))