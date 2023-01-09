import sys

N = sys.stdin.readline()
A = set(sys.stdin.readline().split())

M = sys.stdin.readline()
B = sys.stdin.readline().split()

for i in B:
    sys.stdout.write('1\n') if i in A else sys.stdout.write('0\n')
