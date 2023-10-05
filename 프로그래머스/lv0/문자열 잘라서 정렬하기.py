def solution(myString):
    new_str = myString.split("x")
    new_str.sort()
    return [str for str in new_str if str.strip() != ""]

# def solution(myString):
#     answer = ' '.join(myString.split('x')).split()
#     return sorted(answer)