from collections import Counter

def solution(a, b, c, d):
    counts = Counter([a, b, c, d])

    if len(counts) == 1:
        # 네 주사위에서 나온 숫자가 모두 같다면
        return list(counts.keys())[0] * 1111
    elif len(counts) == 2:
        # 주사위가 두 개씩 같은 값이 나오거나 세 개의 주사위에서 같은 값이 나왔다면
        keys = list(counts.keys())
        values = list(counts.values())
        
        if max(values) == 3:
            # 세 개의 주사위에서 같은 값이 나왔다면
            return (10 * keys[values.index(3)] + keys[values.index(1)]) ** 2
        else:
            # 두 개씩 같은 값이 나왔다면
            return sum(keys) * abs(keys[0] - keys[1])
    elif len(counts) == 3:
        # 어느 두 주사위에서 나온 숫자가 같고 나머지 두 주사위에서 다른 숫자가 나왔다면 
        keys = list(counts.keys())
        values = list(counts.values())
        
        for i in range(len(values)):
            if values[i] == 2: 
                keys.pop(i)
                break
        
        return keys[0] * keys[1]
    else:
       # 네 주사위에 적힌 숫자가 모두 다르다면 
       return min([a,b,c,d])
