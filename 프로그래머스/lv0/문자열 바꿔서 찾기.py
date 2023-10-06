def solution(myString, pat):
    new_str = ""
    
    for i in myString:
        if i == "A":
            new_str += "B"
        elif i == "B":
            new_str += "A"
    
    return 1 if pat in new_str else 0

# def solution(myString, pat):
#     return int(''.join(['A' if i == 'B' else 'B' for i in pat]) in myString)