# https://seongonion.tistory.com/90
import heapq
import sys

input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []

# 왼쪽 힙은 최대힙으로, 큰 값들이 저장되는 오른쪽 힙은 최소힙으로 만들면
# 왼쪽 힙은 pop할 때마다 중간값보다 작은 값들 중 가장 큰 값들부터
# 오른쪽 힙은 pop할 때마다 중간값보다 큰 값들 중 가장 작은 값들부터
for _ in range(n):
    x = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -x)
    else:
        heapq.heappush(right_heap, x)

    # 만약 왼쪽 힙 중 가장 우선순위가 높은 값, 즉 가장 큰 값이
    # 오른쪽 힙의 가장 오선순위가 높은 값은 가장 작은 값보다 클 경우
    # 두 수를 바꾸면 중간값을 기준으로 쭉 나눠놓음
    if left_heap and right_heap and left_heap[0] * -1 > right_heap[0]:
        max_value = heapq.heappop(left_heap)
        min_value = heapq.heappop(right_heap)

        heapq.heappush(left_heap, min_value * -1)
        heapq.heappush(right_heap, max_value * -1)
    print(left_heap[0] * -1)