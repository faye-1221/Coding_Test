origin_l = [1, 1, 2, 2, 2, 8]

l = list(map(int, input().split()))

for i in range(len(l)):
    print(origin_l[i] - l[i], end=' ')