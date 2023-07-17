a = list(input())

l = []
for i in a:
    if i.isupper():
        l.append(i.lower())
    else:
        l.append(i.upper())

print(''.join(l))