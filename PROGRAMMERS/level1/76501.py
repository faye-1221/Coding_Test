def solution(absolutes, signs):
    answer = 0
    for idx, num in enumerate(absolutes):
        if signs[idx]:
            answer += num
        else:
            answer -= num
    return answer