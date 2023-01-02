N = int(input())
l = list()
for i in range(N):
    l.append([])
    x, y = map(int, input().split(' '))
    l[i].append(x)
    l[i].append(y)
l.sort(key=lambda x:(x[0],x[1]))
for i in range(N):
    print(l[i][0], l[i][1])