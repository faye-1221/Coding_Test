from collections import Counter
def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))

    for pho in photo:
        answer2 = 0
        counter = Counter(pho)
        for c in counter:
            if c in dic:
                answer2 += counter[c] * dic[c]
        answer.append(answer2)
    return answer