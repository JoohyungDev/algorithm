def solution(arr):
    num_rows = len(arr)
    num_cols = len(arr[0])

    if num_rows > num_cols:
        for i in range(num_rows):
            arr[i] += [0] * (num_rows - num_cols)
    elif num_cols > num_rows:
        for i in range(num_cols - num_rows):
            arr.append([0] * num_cols)

    return arr
