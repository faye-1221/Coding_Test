# N은 3^k 이므로 다 3씩 끊어서 계산하기
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result = []

def sol(x, y, N):
    find = paper[x][y]
    print(find)
    for i in range(x, x+N):
        for j in range(y, y+N):
            if find != paper[i][j]:
                sol(x, y, N//3)
                sol(x, y+N//3, N//3)
                sol(x+N//3, y, N//3)
                sol(x+N//3, y+N//3, N//3)
                return
    result[find] += 1
    

sol(0, 0, N)
print(result[0])
print(result[1])
print(result[2])