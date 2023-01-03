N = int(input())
l = list()
for i in range(N):
    age, name = map(str, input().split(' '))
    add = {'age':age, 'name':name, 'num':i}
    l.append(add)
l = sorted(l, key = lambda x: (int(x['age']), int(x['num'])))

for i in l:
    print(i['age'], i['name'])