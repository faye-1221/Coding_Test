n = int(input())
l = list(map(int, input().split()))

stack = []
cnt = 1

while l:
    if l[0] == cnt:
        l.pop(0)
        cnt += 1
    else:
        stack.append(l.pop(0))
    
    while stack:
        if stack[-1] == cnt:
            stack.pop()
            cnt += 1
        else:
            break
    
if not stack:
    print("Nice")
else:
    print('Sad')
