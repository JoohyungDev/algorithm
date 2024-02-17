def solution(n):
    # 0부터 n까지의 숫자 리스트 생성
    nums_list = [True] * (n + 1)
    count = 0

    # 0과 1은 소수가 아님
    nums_list[0] = nums_list[1] = False

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(n ** 0.5) + 1):
        # nums_list[i]가 소수인 경우
        if nums_list[i]:
            # i의 배수들은 소수가 아님
            for j in range(i * i, n + 1, i):
                nums_list[j] = False

    # True인 값 세기
    count = sum(nums_list)

    return count