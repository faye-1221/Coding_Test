# https://yuna0125.tistory.com/131
N = int(input())
data = [list(input()) for i in range(N)]
ans = 0
def check(data):
    max_cnt = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if data[i][j] == data[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            
            max_cnt = max(max_cnt, cnt)

        cnt = 1
        for j in range(1, N):
            if data[j][i] == data[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            
            max_cnt = max(max_cnt, cnt)
    return max_cnt

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
            cnt = check(data)
            ans = max(ans, cnt)

            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
        
        if i + 1 < N:
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
            cnt = check(data)
            ans = max(ans, cnt)

            data[i][j], data[i+1][j] = data[i+1][j], data[i][j]

print(ans)