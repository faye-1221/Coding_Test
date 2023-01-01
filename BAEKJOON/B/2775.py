import copy
T = int(input())

for _ in range(T):
    k = int(input()) #k층 = a층 // 0~k층
    n = int(input()) #n호 = b호 // 1~n호

    l1 = list()
    l2 = list()
    for j in range(1, n+1):
        l1.append(j)
    l2 = copy.deepcopy(l1)

    for i in range(k):
        for j in range(0, n):
            l1[j] = sum(l2[:j+1])
        l2 = copy.deepcopy(l1)
    print(l1[-1])
# 1 4 10 20 35
# 1 3 6 10 15
# 1 2 3 4 5