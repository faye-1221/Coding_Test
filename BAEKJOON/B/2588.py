A = int(input())
b = int(input())

for B in map(int, str(b)[::-1]):
    print(A*B)

print(A*b)