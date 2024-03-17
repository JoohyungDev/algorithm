# https://100.pyalgo.co.kr/?page=68#


def solution(data):
    data = list(map(str, data))  # 정수를 문자열로 변환
    # 입력한 x에 대해 2번 반복 [33, 3030, 3434, 55, 99]
    sorted_data = sorted(data, key=lambda x: x * 2, reverse=True)
    # 앞에 오는 0을 제거하기 위함
    return str(int("".join(sorted_data)))


print(solution([3, 30, 34, 5, 9]))
