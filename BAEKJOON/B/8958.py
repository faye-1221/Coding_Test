import sys
N = int(input())
data = []
for _ in range(N):
    data = list(map(str, sys.stdin.readline().rstrip()))

    cnt = 0
    answer = 0

    for i in range(len(data)):
        if data.pop() == 'O':
            cnt += 1
            answer += cnt
        else:
            cnt = 0
    print(answer)
