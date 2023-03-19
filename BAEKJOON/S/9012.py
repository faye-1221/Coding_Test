T = int(input())

for _ in range(T):
    t = list(input())
    stack = []
    yesno = 1
    for i in t:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if not len(stack) == 0:
                stack.pop()
            else:
                yesno = 0

    if(yesno and len(stack) == 0):
        print("YES")
    else:
        print("NO")        
