# https://100.pyalgo.co.kr/?page=18#

def solution(data):
    sorted_data = sorted(data.items(), key=lambda x: x[1],reverse=True)
    selected_data = sorted_data[:3]
    dict_data = dict(selected_data)
    return [str(i[2:])+': '+str(j) for i,j in dict_data.items()]

# heapq 모듈은 리스트를 최소 힙처럼 다룬다! 따라서 빈리스트를 선언하고 추가해야한다
# def solution(data):
#     import heapq
#     heap = []
#     for date, temp in data.items():
#         # 힙에 (온도, 날짜) 튜플을 추가
#         heapq.heappush(heap, (-temp, date))   # (heap,item), item을 heap에 추가
                                                # temp가 -인 이유는 뒤에서 가장 작은 원소를 pop하므로
#     result = []
#     for _ in range(3):
#         temp, date = heapq.heappop(heap)  # heap에서 가장 작은 원소를 pop하고 return
#         result.append(date[2:] + ': ' + str(-temp))   # 2024년이라 하면 앞에 2자리 빼고 출력(24)
        
#     return result