# 풀이 1: 서브태스크 17점
# 주유소의 리터 당 가격이 현재보다 저렴한 지점이 있다면 거기까지의 거리만큼 구매
N = int(input()) # 도시의 개수: 4
roads = list(map(int, input().split())) # 도로의 길이: 2 3 1
costs = list(map(int, input().split()))[:-1] # 주유소의 리터 당 가격: 5 2 4 1 <맨 마지막 지점은 없는거나 마찬가지 아님?>

def fun():
    result = 0
    for i in range(N-1):

        if costs[i] == min(costs[i:]): # 제일 저렴한 구역이라면
            result += (costs[i] * sum(roads[i:]))
            return result
        
        else: # 더 저렴한 곳이 있다면
            result += (costs[i]*roads[i])
print(fun())

# 풀이 2
# 저렴한 가격이 나오면 그만큼 곱한다
N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

def fun():
    result = 0
    min_costs = costs[0]

    for i in range(N-1):
        if min_costs > costs[i]:
            min_costs = costs[i]
        
        result += (min_costs * roads[i])
    return result

print(fun())