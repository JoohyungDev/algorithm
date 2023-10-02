def solution(array, n):
    differ_list = []
    for i in array:
        if i != n:
            differ_list.append(abs(n-i))
        else:
            return i

    min_value = min(differ_list)
    
    # 같은 최소 거리를 갖는 요소들의 인덱스를 저장할 리스트
    min_indexes = [i for i, x in enumerate(differ_list) if x == min_value]
    
    # 해당 인덱스들 중에서 실제 값이 가장 작은 것을 선택하여 반환
    return min(array[i] for i in min_indexes)

# def solution(array, n):
#     array.sort()
#     temp = []

#     for i in array :
#         temp.append( abs(n-i) )

#     return array[temp.index(min(temp))]