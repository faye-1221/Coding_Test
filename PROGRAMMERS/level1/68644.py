from itertools import combinations
def solution(numbers):
    answer = []
    nCr = list(combinations(numbers, 2))
    for i in nCr:
        if sum(i) not in answer:
            answer.append(sum(i))
    return sorted(answer)