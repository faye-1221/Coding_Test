import math
a, b = map(int, input().split(' '))
# gcd = list()
# lcm = list()

# #GCD: 최대공약수
# for i in range(1, min(a, b)+1):
#     if (a % i) == 0 and (b % i) == 0:
#         gcd.append(i)
# print(max(gcd))

# #LCM: 최소공배수
# for i in range(max(a, b), (a*b)+1):
#     if (i % a) == 0 and (i % b) == 0:
#         lcm.append(i)
# print(min(lcm))

print(math.gcd(a, b))
print(math.lcm(a, b))
