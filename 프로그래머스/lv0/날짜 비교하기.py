def solution(date1, date2):
    for i in range(3):
        if date1[i] < date2[i]:
            return 1
        elif date1[i] > date2[i]:
            return 0
    return 0

# def solution(date1, date2):
#     return int(date1 < date2)