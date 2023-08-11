N = int(input())
l = []

for _ in range(N):
    l.append(int(input()))

d = [0]*(N)
max = 0

for i in range(N):
    d[i] = 1
    for j in range(i):
        if l[j] < l[i] and d[i] < d[j] + 1:
            d[i] += 1
    if max < d[i]:
        max = d[i]

print(N - max)
