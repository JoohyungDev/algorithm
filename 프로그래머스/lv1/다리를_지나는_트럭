from collections import deque

#total이 weight이하(다음 트럭이 올라갈 수 있을때) 될 때까지 다음차 대기하는 시간을 추가해야함!! 
def solution(bridge_length, weight, truck_weights):
    answer = 0
    total_weight = 0
    waiting_trucks = deque(truck_weights)
    passing_trucks = deque()
    arrived_trucks = deque()

    while waiting_trucks or passing_trucks:
        answer += 1
        if passing_trucks and passing_trucks[0][1] == answer: # passing_trucks[0][1]이 의미하는 것은 차량 한대가 건너가는데 걸리는 시간값
            truck = passing_trucks.popleft()
            total_weight -= truck[0]
            arrived_trucks.append(truck)

        if waiting_trucks and total_weight + waiting_trucks[0] <= weight:
            truck = waiting_trucks.popleft()
            total_weight += truck
            passing_trucks.append([truck, answer + bridge_length])
            
        print("{0}초후 대기 트럭 리스트입니다. {1}".format(answer,waiting_trucks))
        print("{0}초후 다리 위를 지나가는 트럭 리스트입니다. {1}".format(answer,passing_trucks))
        print("{0}초후 도착한 트럭 리스트입니다. {1}".format(answer,arrived_trucks))   
    return answer