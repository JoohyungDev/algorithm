def solution(board, k):
    result = []
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i+j <= k:
                result.append(board[i][j])
    return sum(result)