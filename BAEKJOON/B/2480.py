from collections import Counter
l = Counter(map(int, input().split()))

most = l.most_common(1)[0]

if most[1] == 3:
    print(10000 + most[0] * 1000)
elif most[1] == 2:
    print(1000 + most[0] * 100)
elif most[1] == 1:
    print(max(l) * 100)