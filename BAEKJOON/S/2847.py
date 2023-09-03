N = int(input())

l = []
for i in range(N):
    l.append(int(input()))

cnt = 0
num = 0

for idx, i in enumerate(l[::-1]):
    if idx == 0:
        num = i
    else:
        if num <= i:
            cnt += (i-num)+1
            num = i - ((i-num)+1)
        else:
            num = i
print(cnt)