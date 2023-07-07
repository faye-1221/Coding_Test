N = int(input())

cnt = 0

def f(string):
    s = None

    for idx, st in enumerate(string):
        if s == None:
            s = string[idx]
        
        if s != st and st in string[0: idx-1]:
            return 0
        else:
            s = string[idx]
    return 1


for _ in range(N):
    string = list(input())

    cnt += f(string)
print(cnt)