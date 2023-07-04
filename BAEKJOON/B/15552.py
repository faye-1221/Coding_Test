import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = sys.stdin.readline().strip().split()
    print(int(a)+int(b))