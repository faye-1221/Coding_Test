# 블랙잭
# 블랙잭은 카드의 합이 21을 넘지 않는 한도에서 합을 최대한으로 만드는 게임
# 1. 각 카드에는 양의 정수가 적혀있다.
# 2. 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓은 후, 숫자 M을 크게 외친다.
# 3. 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 고르고, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야한다.

# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력해라.

# 5,6,7[0,1,2]
# 5,7,8[0,2,3]
# 5,8,9[0,3,4]

# 6,7,8[1,2,3]
# 6,8,9[1,3,4]

# 7,8,9[2,3,4]
# 이런 식으로 완전 탐색을 하면 될듯?

# N, M = map(int, input().split())  # N장의 카드, M에 가까운 숫자 만들기
# array = list(map(int, input().split()))

# loop = N-2  # 주어진 N장에서 3장까지 돌리기

# hap = []
# for i in range(0, loop):
#     for j in range(i+1, N-1):
#         if (array[i]+array[j]+array[j+1] <= M):
#             hap.append(array[i]+array[j]+array[j+1])
#             print(array[i], array[j], array[j+1])


# print(max(hap))


n, m = map(int, input().split())
card = list(map(int, input().split()))
res = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card[i] + card[j] + card[k] > m:
                continue
            else:
                res = max(res, card[i] + card[j] + card[k])

print(res)
