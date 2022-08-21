B = 42
remainder = list()  # 나머지 저장 list

for _ in range(10):
    A = str((int(input()) % B))
    if A not in remainder:
        remainder.append(A)

print(len(remainder))
