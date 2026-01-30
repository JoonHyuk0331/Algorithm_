from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_pair = [[1, w] for w in truck_weights]
    waiting_trucks = deque(truck_pair)
    bridge = deque()

    while True:
        if not bridge and not waiting_trucks:
            return time
        if bridge and bridge[0][0] >= bridge_length:  # 다리를 다 건넌 트럭이 있는지 확인
            bridge.popleft()  # y.다리를 지난 트럭에 옮겨놓기
        # 다리에 올라간 트럭들 시간초 증가
        for bridge_data in bridge:
            bridge_data[0] += 1

        if waiting_trucks:  # 대기 트럭이 있는지 확인
            # y.대기 트럭 다리에 올라갈 수 있는지 확인
            cur_bridge_weight = 0
            for progress, we in bridge:
                cur_bridge_weight += we

            # y.다리에 트럭 올리기
            if cur_bridge_weight + waiting_trucks[0][1] <= weight:
                bridge.append(waiting_trucks.popleft())
        time += 1

print(solution(100	,100,	[10]))