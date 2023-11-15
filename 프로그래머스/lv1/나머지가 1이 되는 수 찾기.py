def solution(n):
    return next(x for x in range(1,n+1) if n%x==1)