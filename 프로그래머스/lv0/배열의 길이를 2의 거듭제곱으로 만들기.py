def solution(arr):
    length = len(arr)
    next_power_of_two = 1
    
    while next_power_of_two < length:
        next_power_of_two *= 2

    if length < next_power_of_two:
        arr.extend([0] * (next_power_of_two - length))

    return arr
