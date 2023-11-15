def solution(arr, divisor):
    result = []
    for i in range(0, len(arr)):
        if arr[i] % divisor == 0:
            result.append(arr[i])
        else:
            pass
    if result == []:
        result.append(-1)
    result.sort()
    return result


# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1] 도 가능
# sorted = 본체 리스트는 내버려두고 정렬된 새로운 리스트를 반환
# for문은 n이 arr안에 있을 때 n을 대입해라 인데, 만약 n이 divisor로 나눠지면 n을 반환하고 나눠지는게 없으면 -1 반환