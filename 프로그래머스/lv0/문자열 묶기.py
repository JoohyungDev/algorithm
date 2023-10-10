def solution(strArr):
    value_counts = {}
    
    for item in strArr:
        len_item = len(item)
        
        if len_item in value_counts:
            value_counts[len_item] += 1
        else:
            value_counts[len_item] = 1
            
    return max(value_counts.values())

# def solution(strArr):
#     a=[0]*31
#     for x in strArr: a[len(x)]+=1
#     return max(a)