import math
m = int(input())
n = int(input())

prime_num = []

def is_prime_number(x):
    if x == 1:
        return False
    # 2부터 x의 제곱근까지의 모든 수 확인
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

for x in range(m, n+1):
    if is_prime_number(x):
        prime_num.append(x)

if prime_num:
    print(sum(prime_num))
    print(min(prime_num))
else:
    print(-1)