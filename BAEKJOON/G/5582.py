from sys import stdin
a = stdin.readline().strip()
b = stdin.readline().strip()


dp = [0] * 1000

for i in range(len(a)):
    mx = 0
    for j in range(len(b)):

        if mx < dp[j]:
            mx = dp[j]
        elif a[i] == b[j]:
            dp[j] = mx + 1

print(max(dp))