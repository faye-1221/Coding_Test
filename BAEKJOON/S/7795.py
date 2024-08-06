T= int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    cnt = 0
    for a in A:
        for b in B:
            if a <= b:
                break
            cnt += 1
    print(cnt)