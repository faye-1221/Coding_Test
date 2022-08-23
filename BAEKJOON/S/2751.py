import sys

N = int(input())
l = list()

for _ in range(N):
    l.append(int(sys.stdin.readline()))

# l.sort()

for i in sorted(l):
    sys.stdout.write('{}\n'.format(i))
