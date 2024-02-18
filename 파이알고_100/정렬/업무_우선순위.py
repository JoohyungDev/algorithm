# https://100.pyalgo.co.kr/?page=7#

def solution(data):
    # 두 번째 인덱스가 작은순으로 정렬
    sorted_data = sorted(data, key=lambda x : x[1])
    
    return [x[0] for x in sorted_data]