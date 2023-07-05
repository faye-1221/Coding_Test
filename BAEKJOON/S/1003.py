# 일단 0과 1이 출력되려면 fib가 1, 0일 때니까...
# fib(1)이면 1을 출력
# fib(0)이면 0을 출력

# 재귀 구조, 마구잡이...
# import sys

# def fib(n):
#     if n == 0:
#         l[0] += 1
#         return 0
#     elif n == 1:
#         l[1] += 1
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# if __name__ == "__main__":

#     l = [[], []]
#     T = int(sys.stdin.readline())

#     for i in range(T):
#         l[0] = 0
#         l[1] = 0
#         n = int(sys.stdin.readline())
#         fib(n)
#         print(l[0], l[1])

# https://bio-info.tistory.com/122
def fib(n):
    zeros = [1, 0, 1]
    ones = [0, 1, 1]
    
    if n >= 3:
        for i in range(2, n):
            zeros.append(zeros[i-1] + zeros[i])
            ones.append(ones[i-1] + ones[i])
    print(f'{zeros[n]} {ones[n]}')

T = int(input())
for _ in range(T):
    N = int(input())
    fib(N)