def solution(lines):
    # 가장 작은점, 큰점 구한 범위 내에서 계산
    line_list = []
    
    for line in lines:
        line_list += line
        
    mx, mn = max(line_list), min(line_list)
    x, y, z = lines
    overlap_line_count = 0
    
    for i in range(mn, mx+1):
        overlap_point_count = 0

        if x[0] <= i < x[1]:
            overlap_point_count += 1
        if y[0] <= i < y[1]:
            overlap_point_count += 1
        if z[0] <= i < z[1]:
            overlap_point_count += 1

        if overlap_point_count >= 2:
            overlap_line_count += 1
        # print(f'i x y z overlap_point_count overlap_line_count', i, x, y, z, overlap_point_count, overlap_line_count)

    return overlap_line_count


# def solution(lines):
#     s1 = set(i for i in range(lines[0][0], lines[0][1]))
#     s2 = set(i for i in range(lines[1][0], lines[1][1]))
#     s3 = set(i for i in range(lines[2][0], lines[2][1]))
#     return len((s1 & s2) | (s2 & s3) | (s1 & s3))