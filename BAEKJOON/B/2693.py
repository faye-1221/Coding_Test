T = int(input())
for i in range(T):
    l = sorted(list(map(int, input().split())))
    print(l[-3])