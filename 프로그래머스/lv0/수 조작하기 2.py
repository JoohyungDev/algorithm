def solution(numLog):
    moves = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    return ''.join(moves[numLog[i] - numLog[i-1]] for i in range(1, len(numLog)))

# def solution(numLog):
#     result = ''
#     for i in range(1,len(numLog)):
#         if numLog[i] == numLog[i-1]+1:
#             result += 'w'
#         elif numLog[i] == numLog[i-1]-1:
#             result += 's'
#         elif numLog[i] == numLog[i-1]+10:
#             result += 'd'
#         elif numLog[i] == numLog[i-1]-10:
#             result += 'a'
#     return result
