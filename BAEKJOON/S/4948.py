import math
n = 123456*2
array = [True for _ in range(n+1)]

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        print(array[n+1:n*2].count(True))