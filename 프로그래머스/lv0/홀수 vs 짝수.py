def solution(num_list):
    odd=0 #홀
    even=0  #짝
    
    for i in range(len(num_list)):
        if i % 2 == 0:
            even += num_list[i]
        else:
            odd += num_list[i]
    return odd if odd > even else even
