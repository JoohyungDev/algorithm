import math

def solution(a, b):
    gcd = math.gcd(a,b) # 최대공약수
    
    if gcd != 1:
        a = a//gcd
        b = b//gcd
    
    prime_factors = []
    i = 2
    
    while i <= b:
        if b % i == 0:
            b /= i
            prime_factors.append(i)
        else:
            i += 1
    
    # print(prime_factors)
    
    for j in prime_factors:
        if j != 2:
            if j != 5:
                return 2
            
    return 1