N, M = map(int, input().split())

l = set()
for i in range(N):
    l.add(input())

l2 = set()
for i in range(M):
    l2.add(input())

result = sorted(list(l & l2))

print(len(result))

for i in result:
    print(i)