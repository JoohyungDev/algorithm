def solution(board):
    n = len(board) # 보드의 크기를 n에 저장

    for y, row in enumerate(board):
        for x, area in enumerate(row):
            
        # 현재 위치에 지뢰가 있으면
            if area == 1:
                
                # 지뢰 주변 8방향 검사
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        ny = y + dy 
                        nx = x + dx
        
                    # 보드 내에 위치하는지 확인
                        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != 1:
                            board[ny][nx] = "X"

    safe_area = sum(area.count(0) for area in board)
    
    return safe_area
