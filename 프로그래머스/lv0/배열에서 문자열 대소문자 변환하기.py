def solution(strArr):
    for i in range(len(strArr)):
        if i%2 != 0:
            strArr[i] = strArr[i].upper()
        else:
            strArr[i] = strArr[i].lower()
    return strArr

# def solution(strArr):
#     return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]