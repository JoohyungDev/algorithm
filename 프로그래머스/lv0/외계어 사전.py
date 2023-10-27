def solution(spell, dic):
    count = 0   # count가 len(spell)과 같으면 그 단어가 있으므로 return 1, 반복문 돌려서 spell의 원소가 있으면 count +=1
    
    for i in dic:
        count = 0
        
        for j in spell:
            if j in i:
                count += 1
            if count == len(spell):
                return 1
    return 2

# def solution(spell, dic):
#     for d in dic:
#         if sorted(d) == sorted(spell):
#             return 1
#     return 2