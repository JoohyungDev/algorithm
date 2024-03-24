# https://100.pyalgo.co.kr/?page=76#


def solution(data):
    A, B = data
    result = []
    i = j = 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1

    while i < len(A):  # If there are remaining elements in A
        result.append(A[i])
        i += 1

    while j < len(B):  # If there are remaining elements in B
        result.append(B[j])
        j += 1

    return result


solution([[-5, 0, 5], [-6, -4, -2, 0, 2, 4]])
