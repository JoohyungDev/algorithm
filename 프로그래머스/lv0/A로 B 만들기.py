from collections import Counter

def solution(before, after):   
    return int(Counter(before) == Counter(after))

# def solution(before, after):
#     return 1 if sorted(before)==sorted(after) else 0