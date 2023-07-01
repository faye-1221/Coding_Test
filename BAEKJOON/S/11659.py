# https://my-coding-notes.tistory.com/212
import sys
N, M = map(int, sys.stdin.readline().split())
n = list(map(int, sys.stdin.readline().split()))

for i in range(N-1):
    n[i+1] += n[i]
n = [0] + n

for _ in range(M):
    a, b = map(int, input().split())
    print(n[b]-n[a-1])