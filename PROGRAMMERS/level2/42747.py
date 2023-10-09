def solution(citations):
    # n 편 중, h번 이상 인용된 논문이 h편 이상
    # and 나머지 논문이 h번 이하 인용시 h의 최댓값이 H-index
    answer = 0
    citations.sort()
    print(citations)
    for i in range(len(citations)):
        print(citations[i], len(citations)-i)
        if citations[i] >= len(citations) - i:
            answer += 1
    return answer
