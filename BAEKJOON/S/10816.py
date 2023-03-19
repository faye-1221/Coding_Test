from collections import Counter

N = int(input())
n = Counter(input().split(' '))

M = int(input())
m = input().split()

for i in m:
    print(n[i])