# 모든 트럭이 다리를 건너는 최단시간은?
from collections import deque
n, w, L = map(int, input().split()) # 트럭의 갯수, 다리의 길이, 다리의 최대하중
a = deque(map(int, input().split())) # 트럭의 무게
# 다리 위에는 단지 w대의 트럭만 동시에 올라갈 수 있다.
# 다리 위에 올라가 있는 트럭들의 무게의 합은 L보다 작거나 같아야한다.
# 다리 위에 완전히 올라가지 못한 트럭의 무게는 다리 위의 트럭들의 무게의 합을 계산할 때 포함하지 않는다고 가정한다.

bridge = deque([0] * w)
total_weight = 0
time = 0

while bridge:
    # 트럭은 무조건 1초에 1칸 이동
    time += 1
    total_weight -= bridge.popleft()

    if a:
        if (total_weight) + a[0] <= L: # L보다 작거나 같다면
            truck = a.popleft()
            bridge.append(truck)
            total_weight += truck
        else: # L보다 크면
            bridge.append(0)
print(time)