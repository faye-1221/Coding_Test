def solution(park, routes):
    # N: 위    
    # S: 아래
    # W: 왼
    # E: 오
    # [y, x]
    
    
    # x, y 좌표 최대 값
    x_max = len(park[0])
    y_max = len(park)
    
    # S의 위치 찾기
    dp = [0, 0]
    for i in park:
        if i.rfind('S') != -1:
            dp[1] = i.rfind('S')
            break
        dp[0] += 1
        
    
    for r in routes:
        way, cnt = r.split()
        
        origin = dp.copy()
        
        for i in range(int(cnt)):
            
            if way == 'N':
                dp[0] -= 1
            elif way == "S":
                dp[0] += 1
            elif way == "W":
                dp[1] -= 1
            elif way == "E":
                dp[1] += 1
            
            if dp[1] < 0 or dp[1] >= x_max or dp[0] < 0 or dp[0] >= y_max or park[dp[0]][dp[1]] == "X":
                dp = origin
                break
    return dp