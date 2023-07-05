import sys
T = int(sys.stdin.readline())

def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(fac(M) // (fac(M-N) * fac(N)))