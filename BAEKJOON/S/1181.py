N = int(input())
alpha = list()
for i in range(0, N):
    alpha.append(input())

alpha = list(set(alpha))
alpha.sort(key=len)

for i in range(0, len(alpha)):
    print(alpha[i])