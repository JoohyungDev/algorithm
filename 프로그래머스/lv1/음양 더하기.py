def solution(absolutes, signs):
    total = 0
    
    for idx,i in enumerate(absolutes):
        if signs[idx] == True:
            total += i
        else:
            total -= i
    return total

# def solution(absolutes, signs):
#     answer=0
#     for absolute,sign in zip(absolutes,signs):
#         if sign:
#             answer+=absolute
#         else:
#             answer-=absolute
#     return answer