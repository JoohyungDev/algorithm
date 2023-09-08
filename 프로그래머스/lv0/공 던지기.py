def solution(numbers, k):
    numbers *= k
    numbers = numbers[0::2]
    return numbers[k-1]

# def solution(numbers, k):
#     return numbers[2 * (k - 1) % len(numbers)]
