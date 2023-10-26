import sys
import math
input = sys.stdin.readline
limit = 1000000

array = [True for _ in range(limit + 1)]

# 에라토스테네스의 체 알고리즘 
for i in range(2, int(math.sqrt(limit)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인
    if array[i] == True: # i가 소수인 경우
        # i를 제외한 i의 모든 배수를 지우기
        j = 2 
        while i * j <= limit:
            array[i * j] = False
            j += 1

array[0] = False
array[1] = False

while True:
    n = int(input())
    if n == 0:
        break
    
    result = 0
    for a in range(2, n):
        if array[a] and array[n-a]:
            result = a
            print(f"{n} = {result} + {n-result}")
            break

    if result == 0:
        print("Goldbach's conjecture is wrong.")