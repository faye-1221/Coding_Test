n, m = map(int, input().split())

# RecursionError
# def dfs(i, j, c):
#     if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
#         return c

#     grid[i][j] = '0'
#     c += 1

#     c = dfs(i + 1, j, c)
#     c = dfs(i - 1, j, c)

#     c = dfs(i, j + 1, c)
#     c = dfs(i, j - 1, c)
#     return c

def dfs_iterative(i, j):
    stack = [(i, j)]
    c = 0

    while stack:
        x, y = stack.pop()
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
            continue

        grid[x][y] = '0'
        c += 1

        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))

    return c

grid = []
for i in range(n):
    grid.append(input().split())

count = 0
max_count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '1':
            c = dfs_iterative(i, j)
            if max_count < c:
                max_count = c
            count += 1

print(count, max_count, sep="\n")