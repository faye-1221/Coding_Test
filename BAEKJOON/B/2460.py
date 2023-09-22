l = [0]
for i in range(10):
    down, up = map(int, input().split())
    l.append((l[-1]-down)+up)
print(max(l))