def solution(numlist, n):
    # numlist의 각 원소 x에 대해 n과 x의 절대값 차이와 -x를 튜플로 반환
    # 첫 번째 원소인 절대값 차이를 기준으로 오름차순 정렬하고, 절대값 차이가 같을 경우 두 번째 원소인 -x를 기준으로 내림차순 정렬
    numlist.sort(key=lambda x: (abs(x-n), -x))
    return numlist
