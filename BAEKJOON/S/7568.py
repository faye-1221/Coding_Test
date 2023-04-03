N = int(input())
l = list()
for _ in range(N):
    x, y = map(int, input().split(' '))
    l.append([x, y])

score = [1 for x in range(len(l))]

for i in range(0, len(l)):
    for j in range(0, len(l)):
        if i != j:
            if (l[i][0] < l[j][0]) and (l[i][1] < l[j][1]):
                score[i] += 1
print(*score)
