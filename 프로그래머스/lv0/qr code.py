def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    return answer

# def solution(q, r, code):
#     return code[r::q]

# def solution(q, r, code):
#     return ''.join(code[i] for i in range(r, len(code), q))
