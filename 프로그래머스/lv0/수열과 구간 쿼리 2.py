def solution(arr, queries):
    result = []
    for s,e,k in queries:
        # s부터 e까지의 범위에서 arr을 슬라이싱하고, 그 중 k보다 큰 값들만 골라서 리스트 생성
        filtered_list = [i for i in arr[s:e+1] if i > k]
        # 필터링된 리스트가 비어 있지 않으면 가장 작은 값을 결과에 추가
        if filtered_list:
            result.append(min(filtered_list))
        # 필터링된 리스트가 비어 있으면 -1을 결과에 추가
        else:
            result.append(-1)
    return result
        