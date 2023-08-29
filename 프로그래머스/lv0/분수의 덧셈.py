import math

def solution(numer1, denom1, numer2, denom2):
    final_num = numer1 * denom2 + numer2 * denom1  # 분자의 합을 구함
    final_den = denom1 * denom2  # 분모의 곱을 구함
    
    gcd_value = math.gcd(final_num, final_den)  # 최대공약수 계산
    
    if gcd_value != 1:
        final_num //= gcd_value  # 분자를 최대공약수로 나눔
        final_den //= gcd_value  # 분모를 최대공약수로 나눔
    
    return [final_num, final_den]
