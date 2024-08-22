N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

# A = 1 1 1 6 0
# B = 2 7 8 3 1
# -> 18
'''
A의 수를 재배열
작은 값일 수록 B의 최댓값에 곱하기

1 1 0 1 6
2 7 8 3 1
-> 2, 7, 0, 3, 6 -> 18
'''
# A = 1 1 3
# B = 10 30 20
# -> 80
'''
10 30 20
3 1 1
-> 30, 30, 20 -> 80
'''

'''
A를 정렬
B를 거꾸로 정렬
'''
result = 0
for i in range(N):
    result += A[i] * B[i]
print(result)

# 순서를 기억하는 값을 가지고있고, 정렬하면 시간복잡도가 높아짐
# 그럼 순서를 기억하는 값도 없고, 정렬을 하지 않는 방식은?

# 다른 사람 코드
# n = int(input())

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# s=0
# for i in range(n):
#    s+= min(a) * max(b)
#    a.pop(a.index(min(a)))
#    b.pop(b.index(max(b)))

# print(s)

'''
내가 짠 코드 O(n log n) -> sorted: O(n log n)팀소트, for: O(n) -> O(n log n)
다른 사람이 짠 코드 O(n^2) -> min/max: O(n), pop/index/max/min: O(n) -> O(n^2)
'''