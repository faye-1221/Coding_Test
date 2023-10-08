from collections import deque
def solution(priorities, location):
    end = len(priorities)
    que = deque([x for x in range(end)])
    priorities = deque(priorities)
    
    result = []
    
    while len(result) != end:
        ready = priorities.popleft()
        q = que.popleft()
        
        if priorities and ready < max(priorities):
            que.append(q)
            priorities.append(ready)
        else:
            result.append(q)
    return result.index(location)+1

# 다른 사람 코드: queue를 만든 과정, any 사용, location과 같을 때 계속 더하던 answer을 리턴하는 부분이 배워야 할 부분.
def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0

    while True:
        cur = queue.pop(0)

        if any(cur[1] < q[1] for q in queue): # any(): 하나라도 True인 게 있으면 True // max의 시간복잡도 O(n), any는 조건을 만족하는 값을 찾으면 중단하므로 max보다는 좋은듯?
            queue.append(cur) # 더 큰 값이 있으면 queue에 다시 넣기
        else: # 더 큰 값이 없으면
            answer += 1 # 프로세스를 실행하면 answer += 1
            if cur[0] == location: # 찾는 값이면 answer 리턴
                return answer # answer은 프로세스가 몇 번째로 실행되는지 출력