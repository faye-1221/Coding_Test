# https://velog.io/@kimdukbae/BOJ-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-Python
import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split())) # +, -, *, //

maximum = -1e9
minimum = 1e9

def back(depth, total, plus, minus, multiply, divide):
    global maximum, minimum

    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if plus:
        back(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    
    if minus:
        back(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)

    if multiply:
        back(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)

    if divide:
        back(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide - 1)

back(1, nums[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)