import heapq
def solution(scoville, K):
    heapq.heapify(scoville) # list를 heaq로 변경
    answer = 0
    
    while scoville[0] < K:
        # heaq는 작은 순서대로 자동 정렬이므로 제일 작은 값이 K 보다 작을 경우 계속 반복
        
        if len(scoville) == 1: # 음식 갯수가 1일 경우 -1 반환
            return -1
        
        first = heapq.heappop(scoville) # 제일 작은 값 pop
        two = heapq.heappop(scoville) # 또 작은 값 pop
        
        heapq.heappush(scoville, first+(two*2)) # push (append 아니니까 명심하기...!)
        
        answer += 1
        
    return answer