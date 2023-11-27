def solution(n, arr1, arr2):
    answer = ['']*n

    for idx in range(n):
        # bin1, bin2 계산과 동시에 이진수 변환
        bin1 = format(arr1[idx], '0' + str(n) + 'b')
        bin2 = format(arr2[idx], '0' + str(n) + 'b')

        for i in range(n):
            # bin1, bin2 각 원소 비교
            if bin1[i] == '1' or bin2[i] == '1':
                answer[idx] += '#'
            else:
                answer[idx] += ' '

    return answer
