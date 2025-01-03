# 시간 초과
# import sys
# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     l = list(map(int, input().split()))
    
#     result = 0
#     cart = []

#     for idx, i in enumerate(l):
#         # 마지막 위치면
#         if idx == len(l)-1:
#             for c in cart:
#                 result += (i-c)
#             break
        
#         # 현재 값보다 남은 값이 더 크면 cart에 넣기
#         if i < max(l[idx+1:]):
#             cart.append(i)
#         else:
#             if cart:
#                 for c in cart:
#                     result += (i-c)
#                     cart = []

#     print(result)

# 2안-시간초과
# import sys
# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     l = list(map(int, input().split()))
    
#     max_value = 0
#     result = 0
#     cart = []

#     for idx, i in enumerate(l):
        
#         # 마지막 위치면
#         if idx == len(l)-1:
#             break
        
#         max_value = max(l[idx+1:])
#         if i < max_value:
#             result += (max_value - i)
#         else:
#             max_value = 0

#     print(result)

# 거꾸로: https://velog.io/@yoonuk/%EB%B0%B1%EC%A4%80-11501-%EC%A3%BC%EC%8B%9D-Python
T = int(input())

for t in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    money = 0

    maxPrice = 0

    for i in range(len(price)-1, -1, -1):
        if price[i] > maxPrice:
            maxPrice = price[i]
        else: # 현재 가격이 현재 최대 가격보다 작다면 차익 실현
            money += maxPrice - price[i]

    print(money)

# 기존 풀었던 방식에서 max가 오래 걸렸다. 그래서 거꾸로 풀 것...