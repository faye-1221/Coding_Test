from collections import deque

'''
연산
1. 뒤에 A를 추가
2. 뒤에 B를 추가하고 문자열 뒤집기
A -> BABA
'''
S = list(input())
T = list(input())

def func(T):
    if T == S:
        print(1)
        exit()
    
    if len(T) == 0:
        return
    
    if T[-1] == 'A':
        new_T = T[:-1]
        func(new_T)
    
    if T[0] == 'B':
        new_T = T[1:]
        new_T.reverse()
        func(new_T)

func(T)
print(0)
