def solution(dots):
    a = dots[0]
    b = dots[1]
    c = dots[2]
    d = dots[3]

    # ((a,b),(c,d)), ((a,c),(b,d)), ((b,c),(a,d))
    # slope 1
    slope1 = abs((b[1]-a[1]) / (b[0]-a[0]))
    slope1_1 = abs((d[1]-c[1]) / (d[0]-c[0]))
    
    slope2 = abs((c[1]-a[1]) / (c[0]-a[0]))
    slope2_1 = abs((d[1]-b[1]) / (d[0]-b[0]))
    
    slope3 = abs((c[1]-b[1]) / (c[0]-b[0]))
    slope3_1 = abs((d[1]-a[1]) / (d[0]-a[0]))
    
    if slope1 == slope1_1 or slope2 == slope2_1 or slope3 == slope3_1:
        return 1
    return 0