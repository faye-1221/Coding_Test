h, m = map(int, input().split())
c = int(input())

m += c

qu = int(m/60) # 60을 넘으면
m = m - (qu*60)

while qu > 0:
    h += 1
    qu -= 1
    if h >= 24:
        h = 0


print(h, m)