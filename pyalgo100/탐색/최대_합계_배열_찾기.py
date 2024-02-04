def solution(data):
    # 초기값으로 주어진 length 만큼의 합을 초기값으로 
    my_list, length = data
    max_sum = sum(my_list[:length])
    # 한칸씩 오른쪽으로 이동하며 max_sum보다 값이 크면 그 값을 max_sum에 저장
    # 슬라이싱은 배열의 길이를 벗어나면 무시
    for idx, _ in enumerate(my_list,1):
        if sum(my_list[idx:idx+length]) > max_sum:
            max_sum = sum(my_list[idx:idx+length])
    return max_sum