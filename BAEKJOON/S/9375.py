T = int(input())

for _ in range(T):
    ct = int(input())
    clothes = {}

    for _ in range(ct):
        n, t = input().split()
        clothes[t] = clothes.get(t, []) + [n]
    
    cnt = 1
    for key in clothes.keys():
        cnt *= len(clothes[key]) + 1

    print(cnt-1)