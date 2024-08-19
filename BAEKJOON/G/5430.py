from collections import deque
import ast
import sys

input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    p = input().strip()  # 함수
    n = int(input())  # 배열에 들어있는 수의 개수
    array_input = input().strip()

    if array_input == "[]":
        x = deque()
    else:
        x = deque(map(int, array_input[1:-1].split(',')))

    reverse_flag = False
    error_flag = False

    for command in p:
        if command == "R":
            reverse_flag = not reverse_flag
        elif command == "D":
            if not x:
                print("error")
                error_flag = True
                break
            else:
                if reverse_flag: # reverse를 계속하면 시간 초과라서 pop을 할 수 있도록 flag 저장
                    x.pop()
                else:
                    x.popleft()

    if not error_flag:
        if reverse_flag:
            x.reverse()
        print("[" + ",".join(map(str, x)) + "]")