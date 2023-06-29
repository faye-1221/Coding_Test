def zero_check(fac):
    cnt = 0
    for i in fac:
        if i == '0':
            cnt += 1
        else:
            return cnt

N = int(input())
fac = 1
for i in range(1, N+1):
    fac *= i

fac = list(str(fac))
fac.reverse()

print(zero_check(fac))
