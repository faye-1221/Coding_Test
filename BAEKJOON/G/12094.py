'''
2가지 연산
1. 문자열 뒤에 A를 추가한다
2. 문자열을 뒤집고 뒤에 B를 추가한다
S -> T로 바꿀 수 있는지 True = 1, False = 0
---
T -> S로 한다면
T의 마지막 문자가 A라면 제거
T의 마지막 문자가 B라면 제거하고 reverse
T == S 일때 변환되었으면 return 1
'''
S = list(input())
T = list(input())

while len(T) != len(S):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()


if T == S:
    print(1)
else:
    print(0)