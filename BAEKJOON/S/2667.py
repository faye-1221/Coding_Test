from collections import Counter
cnt = 1
count = []

def dfs(i, j):
    global cnt
    global count

    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '0'
    count.append(str(cnt))

    dfs(i + 1, j)
    dfs(i - 1, j)

    dfs(i, j + 1)
    dfs(i, j - 1)


wh = int(input())
grid = []
for i in range(wh):
    grid.append(list(input()))
    
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '1':
            cnt += 1
            dfs(i, j)
count = Counter(count).most_common()
print(len(count))
for _, i in count[::-1]:
    print(i)