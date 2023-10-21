import sys

input = sys.stdin.readline
N = int(input())

l = []
for i in range(N):
    l.append(int(input()))

l.sort()

for i in l:
    print(i)