import sys

input = sys.stdin.readline

N = int(input())
l = []

for i in range(N):
    l.append(int(input()))

l.sort(reverse=True)

for j in l:
    print(j)