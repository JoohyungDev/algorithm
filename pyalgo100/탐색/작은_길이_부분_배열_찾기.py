def solution(data):
    # 배열과 타겟숫자를 언패킹(my_list, target)
    # start, end (인덱스변수), result 초기화
    # 현재 배열의 합계를 저장할 변수 초기화
    my_list, target = data
    start, end, result, current_sum = 0, 0, 0, 0

    # 배열의 끝값이 배열 전체길이와 같아질때까지 반복 
    while end < len(my_list):
        # 현재 끝 값을 부분 배열 합에 더함
        current_sum += my_list[end]

        # 현재 배열의 합이 target이상이면 반복
        while current_sum >= target:
            result = min(result, end - start + 1) if result != 0 else end - start + 1
            # target이상이면서 더 작은 배열을 찾기 위함
            # start가 1칸 이동할 예정이므로 그 값은 합에서 뺀다
            current_sum -= my_list[start]
            start += 1

        # 현재 배열의 합이 target 미만이면 배열의 끝값 +1
        end += 1

    return result if result != 0 else 0


# def min_sub_array_len(nums, s):
#     start = 0
#     sum = 0
      # 어떤 실수보다도 큰 값. 비교를 위함
#     min_len = float('inf')

#     for end in range(len(nums)):
#         sum += nums[end]
#         while sum >= s:
#             min_len = min(min_len, end - start + 1)
#             sum -= nums[start]
#             start += 1

#     return min_len if min_len != float('inf') else 0
