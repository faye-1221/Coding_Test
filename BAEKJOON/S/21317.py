N = int(input())
energy = []
for i in range(N-1):
    small, long = map(int, input().split())
    energy.append([small, long])
long_long_energy = int(input())

result = []


def dfs(start = 0, path = []):


    for i in range(start, N-1):
        small = dfs(i+1, path + energy[i][0])
        long = dfs(i+1, path + energy[i][1])
        long_long = dfs(i+1, path + long_long_energy)

dfs()