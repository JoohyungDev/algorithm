from collections import Counter,deque

def solution(A, B):
    queue = deque(A)
    count = 0 

    if Counter(A) == Counter(B):
        for i in range(len(A)):
            if ''.join(queue) == B:
                return count
            else:
                queue.appendleft(queue[-1])
                queue.pop()
                count += 1
    return -1

# from collections import deque

# def solution(A, B):
#     a, b = deque(A), deque(B)
#     for cnt in range(0, len(A)):
#         if a == b:
#             return cnt
#         a.rotate(1)
#     return -1