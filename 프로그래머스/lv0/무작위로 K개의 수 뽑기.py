def solution(arr, k):
    result = []
    # 일정한 범위에서 무작위로 수를 뽑기
    # 지금까지 나온적 없는 수이면 배열 맨뒤에 추가
    # 어떤 수가 무작위로 주어질지 알고 있다
    # 무작위의 수는 arr에 저장된 순서대로 주어질 예정
    # 완성 배열의 길이 < k 나머지 값을 전부 -1로 채워 return
    arr = list(dict.fromkeys(arr))
    result = arr

    if len(arr) < k:
        for i in range(k-len(arr)):
            result.append(-1)
    elif len(arr) > k:
        for i in range(len(arr)-k):
            del result[-1]
            
    return result
   