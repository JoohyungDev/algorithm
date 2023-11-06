def solution(bin1, bin2):
    decimal_number1 = int(bin1, 2)
    decimal_number2 = int(bin2, 2)
    
    result = decimal_number1+decimal_number2
    
    return (bin(result)[2:])

# def solution(bin1, bin2):
#     answer = bin(int(bin1,2) + int(bin2,2))[2:]
#     return answer