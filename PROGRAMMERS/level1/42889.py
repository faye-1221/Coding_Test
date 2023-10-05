def solution(N, stages):
    level = {}
    t = len(stages)
    
    for i in range(1, N+1):
        if t == 0:
            level[i] = 0
        else:
            level[i] = stages.count(i)/t
            t -= stages.count(i)
    
    return sorted(level, key=lambda x:level[x], reverse=True)    