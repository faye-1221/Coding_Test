T = int(input())

for i in range(T):
    N = int(input())
    l = list(map(int, input().split()))

    for i in range(1, len(l)):
        if l[i-1] > 0:
            l[i] = l[i-1] + l[i]
        else:
            l[i] = l[i]
    
    print(max(l))