A, B = map(str, input().split(' '))
a = "".join(reversed(A))
b = "".join(reversed(B))
print(max(a, b))
# join은 list, tuple을 str로 만들 수 있다..!
