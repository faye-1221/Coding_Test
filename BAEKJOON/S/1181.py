N = int(input())
alpha = list()
for i in range(0, N):
    word = str(input())
    alpha.append((word, len(word)))

alpha = list(set(alpha))
alpha.sort(key=lambda x: (x[1], x[0]))

for i in alpha:
    print(i[1])