def solution(data):
    my_str, target = data
    if target in my_str:
        return my_str.index(target)
    return False