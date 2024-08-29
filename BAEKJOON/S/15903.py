n, m = map(int, input().split()) # 카드의 개수, 카드 합체 횟수
l = list(map(int, input().split())) # 맨 처음 가드의 상태를 나타내는 n개의 자연수
# 첫 번째 줄에 만들 수 있는 가장 작은 점수를 출력

l.sort(reverse=True)

for _ in range(m):
    x = l.pop()
    y = l.pop()
    xy = x + y
    l.append(xy)
    l.append(xy)
    l.sort(reverse=True)
print(sum(l))

# 초기 정렬 O(n log n)
# for 루트 O(n log n)
# print O(n)
# 전체 O(m * n log n)
