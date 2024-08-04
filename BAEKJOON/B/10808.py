S = input()
result = []
for i in range(97, 123):
    result.append(S.count(chr(i)))

print(*result)