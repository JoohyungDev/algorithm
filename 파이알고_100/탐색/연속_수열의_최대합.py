def solution(data):
    max_sum = current_sum = data[0]
    
    for num in data[1:]:
        print(num, current_sum + num)
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
        
