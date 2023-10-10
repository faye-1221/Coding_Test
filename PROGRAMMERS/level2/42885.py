from collections import deque
def solution(people, limit):
    
    queue = deque(sorted(people))
    
    L = []
    count = 0
    
    while queue:
        if len(queue) > 1:
            min = queue.popleft()
            max = queue.pop()
            
            if min+max > limit:
                L.append(max)
                queue.appendleft(min)
            else:
                count += 1
        else:
            queue.popleft()
            count += 1
    return count + len(L)

# 다른 사람 풀이
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer