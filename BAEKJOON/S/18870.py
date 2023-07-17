import sys
n = int(input())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

numset = list(set(numbers))
numset.sort()

numdict = {}
for i in range(len(numset)):
    numdict[numset[i]] = i

for i in numbers:
    print(numdict[i], end=' ')