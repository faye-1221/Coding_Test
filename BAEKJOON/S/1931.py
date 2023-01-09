N = int(input())
l = []
l2 = []
for _ in range(N):
    start, end = map(int, input().split())
    l.append([start, end])
l.sort(key = lambda x: (x[1], x[0]))

for i in l:
    if len(l2) == 0:
        l2.append(i)
    else:
        end = l2[-1][1]
        if end <= i[0]:
            l2.append(i)
# print(l)
# print(l2)
print(len(l2))

# 11
# 1 4 -> 1, 3
# 3 5 -> 3, 2
# 0 6 -> 0, 6
# 5 7 -> 5, 2
# 3 8 -> 3, 5
# 5 9 -> 5, 4
# 6 10 -> 6, 4
# 8 11 -> 11, 3
# 8 12 -> 8, 4
# 2 13 -> 2, 11
# 12 14 -> 12, 2
# (1,4), (5,7), (8,11), (12,14) 


# 5
# 6 7
# 6 6
# 5 6
# 5 5
# 7 7
# -> 5