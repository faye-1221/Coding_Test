def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        print(t[i:i+len(p)])
        if t[i:i+len(p)] <= p:
            answer += 1
    return answer