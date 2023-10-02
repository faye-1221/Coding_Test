def solution(s):
    answer = ''
    for i in s.split(' '):
        for idx, j in enumerate(i):
            if idx % 2 == 0:
                j = j.upper()
            else:
                j = j.lower()
            answer += j
        answer += ' '
    return answer[:-1]