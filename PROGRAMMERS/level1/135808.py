def solution(k, m, score): # 사과 최대 점수, 한 상자에 들어가는 사과의 수
    result = []
    score.sort()
    
    a, d = divmod(len(score), m) # 몫 나머지
    
    start = d
    for i in range(a):
        result.append(score[start:(start+m)])
        start += m
        
    # 최저 사과 점수 x 한 상자에 담긴 사과 개수 x 상자의 개수
    answer = 0
    for re in result:
        answer += min(re) * m
    
    return answer
