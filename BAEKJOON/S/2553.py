import sys
N = int(sys.stdin.readline())

f = 1
for i in range(1, N+1):
    f *= i

f = list(str(f))
while True:
    if f[-1] != '0':
        print(f[-1])
        break
    else:
        f.pop(-1)