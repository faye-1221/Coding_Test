from collections import deque

s = deque(input())

def f(s):
    while len(s) > 1:
        if s[0] != s[-1]:
            return False
        s.pop() 
        s.popleft()
    return True
        
if f(s):
    print(1)
else:
    print(0)