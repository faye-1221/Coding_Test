w, h = -1, -1

def dfs(i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
        return
    
    grid[i][j] = '0'

    dfs(i + 1, j)
    dfs(i - 1, j)

    dfs(i, j + 1)
    dfs(i, j - 1)

    dfs(i - 1, j - 1)
    dfs(i - 1, j + 1)

    dfs(i + 1, j - 1)
    dfs(i + 1, j + 1)

while(w != 0 and h != 0):
    w, h = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(list(input().split()))
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    if w != 0 and h != 0:
        print(count)