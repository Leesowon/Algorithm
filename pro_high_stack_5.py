# 2024-10-16

from collections import deque
def solution(bridge_length, weight, trucks):
    time = 0
    bridge = deque([0] * bridge_length) # 다리 상태
    trucks = deque(trucks) # 대기 트럭 큐
    current_weight = 0 # 현재 다리 위의 총 무게

    while trucks or current_weight > 0 : # 대기 트럭이 있거나, 대기 트럭이 없다면 다리에서 다 내려갈때까지
        time += 1 # 트럭이 다리를 모두 내려울 때까지 시간이 경과됨

        # 다리에서 맨 앞의 트럭이 내려옴 / 만약 맨 앞에 트럭이 없었다면 아무 일도 일어나지 않음 (-0)
        exited_truck = bridge.popleft()
        current_weight  -= exited_truck

        # 대기 중인 트럭이 다리 위에 올라갈 수 있는가?
        if trucks and current_weight + trucks[0] <=  weight :
            truck = trucks.popleft()
            bridge.append(truck)
            current_weight += truck
        else : # 다리 위에 못올라가면 빈 공간 유지
            bridge.append(0)

    return time

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))