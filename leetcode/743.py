class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 큐 변수: [(소요 시간, 정점)]
        Q = [(0, k)]

        dist = collections.defaultdict(int)

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q) # Q(힙)에서 가장 작은 원소 삭제 후에 리턴
            if node not in dist: # dist에 node가 없다면
                dist[node] = time # dist에 node 추가
                for v, w in graph[node]: # 그래프 인접리스트 for문
                    # time에 인접리스트의 소요시간 추가 후 Q에 다시 저장
                    alt = time + w 
                    heapq.heappush(Q, (alt, v))
        
        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1