from itertools import combinations
l = []
for i in range(9):
    l.append(int(input()))

per = list(combinations(l, 7))

for i in per:
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break