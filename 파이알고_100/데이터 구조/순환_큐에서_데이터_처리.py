# https://100.pyalgo.co.kr/?page=46#

from collections import deque

def process_commands(size, commands):
    queue = deque(maxlen=size)
    result = []

    for command in commands:
        if command.startswith('insert'):
            _, element = command.split()
            queue.append(element)
            result.append(None)
        elif command == 'delete':
            if queue:
                queue.popleft()
            result.append(None)
        elif command.startswith('search'):
            _, element = command.split()
            result.append(element in queue)

    return result

# def solution(data):
#     from collections import deque
#     size, commands = data['size'], data['commands']
#     queue = deque(maxlen=size)
#     _print = []
#     for i in commands:
#         if i.split()[0] != 'delete':
#             command, num = i.split()[0], i.split()[1]
#         else:
#             command = i
#         if command == 'insert':
#             queue.append(num)
#             _print.append(None)
#         elif command == 'search':
#             if num in queue:
#                 _print.append(True)
#             else:
#                 _print.append(False)
#         elif command == 'delete':
#             queue.popleft()
#             _print.append(None)
#     return _print

# solution({'size': 3, 'commands': ['insert 1', 'insert 2', 'insert 3', 'insert 4', 'search 3', 'delete', 'search 3']})