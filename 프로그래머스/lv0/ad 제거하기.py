def solution(strArr):
    result = []
    for i in strArr:
        if i.count("ad") >= 1:
            pass
        else:
            result.append(i)
    return result

# def solution(strArr):
#     return [word for word in strArr if 'ad' not in word]