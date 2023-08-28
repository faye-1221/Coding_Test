n = int(input())

n2 = n

for i in range(n):
    for j in range(n2):
        print("*", end="")
    n2 -= 1
    print()