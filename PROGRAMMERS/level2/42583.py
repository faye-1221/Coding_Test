def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length # 다리를 우선 길이만큼 0으로 세팅
    cur_weight = 0
    truck_weights = truck_weights[::-1] # 리스트 뒤집어서 pop()으로 사용

    while truck_weights: # 트럭이 남아있을때까지 반복
        answer += 1 # 반복문이 한번 돌 때마다 1초 증가
        cur_weight -= bridge.pop(0) # 다리 위에서 트럭 한대가 빠져나가면 무게 빼기

        # 만약 (현재 무게)가 (트럭이 한대 더 들어와도 다리가 버틸 수 있는 무게게)보다 적으면 트럭을 한 대 추가, 아니면 0으로 세팅
        w = truck_weights.pop() if cur_weight + truck_weights[-1] <= weight else 0

        
        cur_weight += w # 다리 무게에 w를 추가

        bridge.append(w) # 다리에 w를 추가

    return answer + len(bridge)