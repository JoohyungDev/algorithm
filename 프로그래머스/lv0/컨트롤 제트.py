def solution(s):
    total = 0
    s= s.split()
    
    for i in s:
        if i == "Z":
            total -= before_str
        else:
            total += int(i)
            before_str = int(i)
    return total