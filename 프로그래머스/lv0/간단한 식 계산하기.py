def solution(binomial):
    a = int((binomial.split())[0])
    op = (binomial.split())[1]
    b = int((binomial.split())[2])
    
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    else:
        return a*b
    