def solution(s):
    last_position = {}  # 각 문자의 마지막 위치를 저장할 딕셔너리
    result = [-1]*len(s)  # 결과를 저장할 리스트

    for idx, char in enumerate(s):
        if char in last_position:  # 만약 이전에 같은 문자가 나왔다면
            result[idx] = idx-last_position[char]  # 그 위치를 결과에 추가
        last_position[char] = idx  # 현재 문자의 위치를 저장

    return result