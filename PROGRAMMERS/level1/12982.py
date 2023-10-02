def solution(d, budget):
    d.sort()
    result = 0
    for i in d:
        if budget - i >= 0:
            budget -= i
            result += 1
    return result