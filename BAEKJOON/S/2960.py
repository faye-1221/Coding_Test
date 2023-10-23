N, K = map(int, input().split())
l = [i for i in range(2, N+1)]

result = []
for i in range(len(l)):
    if l[i] != 0:
        div = l[i]
        result.append(l[i])
        l[i] = 0
        for j in range(i+1, len(l)):
            if l[j] != 0 and l[j]%div == 0:
                result.append(l[j])
                l[j] = 0

print(result[K-1])

# 다른 사람 코드
N, K = map(int, input().split())
tmp = 0
sieve = [True] * (N + 1)
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if sieve[j] != False:
            sieve[j] = False
            tmp += 1
            if tmp == K:
                print(j)