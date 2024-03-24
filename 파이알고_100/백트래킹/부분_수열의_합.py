# https://100.pyalgo.co.kr/?page=99#


def solution(data):
    nums, target = data
    count = 0

    def backtrack(start, current_sum):
        nonlocal count
        if current_sum == target:
            count += 1
            return

        if current_sum > target:
            return

        for i in range(start, len(nums)):
            backtrack(i + 1, current_sum + nums[i])

    backtrack(0, 0)
    return count


solution(([1, 2, 3, 4, 5], 7))
