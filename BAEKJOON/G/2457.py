import sys
input = sys.stdin.readline

n = int(input().strip())
flowers = []

for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    flowers.append((sm * 100 + sd, em * 100 + ed))

flowers.sort()

start_date = 301
end_date = 1130 
max_end = 0       # 현재 선택된 꽃들로 덮을 수 있는 가장 마지막 날짜
count = 0         # 선택된 꽃의 수
i = 0             # flowers 리스트의 인덱스

while start_date <= end_date:
    found = False

    # 현재 날짜(start_date) 이전에 피는 꽃 중 가장 늦게 지는 꽃 선택
    while i < len(flowers) and flowers[i][0] <= start_date:
        max_end = max(max_end, flowers[i][1])
        i += 1
        found = True
    
    if not found:  # start_date를 덮을 꽃이 없으면 실패
        count = 0
        break

    # 새로운 꽃을 선택했으므로 날짜 갱신 및 카운트 증가
    start_date = max_end
    count += 1

# 결과 출력
print(count if start_date > end_date else 0)
