N = int(input())
l = list()
for i in range(N):
    x, y = map(int, input().split(' '))
    l.append([])
    l[i].append(x)
    l[i].append(y)

l.sort(key = lambda x: (x[1],x[0]))

for i in range(N):
    print(l[i][0], l[i][1])