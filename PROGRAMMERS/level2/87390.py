def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        v = max(i//n, i%n) + 1
        # x=i//n, y=i%n | x, y 중에 큰 수를 구해 +1을 해서 값으로 넣어줌
        answer.append(v)
    return answer