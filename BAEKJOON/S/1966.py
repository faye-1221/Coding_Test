from collections import Counter

# 테스트케이스의수
T = int(input())

for _ in range(T):
    # 문서의 갯수, 몇 번째로 인쇄되었는지 궁금한 문서
    N, M = map(int, input().split())
    # N개 문서의 중요도
    importance = list(map(int, input().split()))
    document = [x for x in range(N)]

    document[M] = 'target'
    
    order = 0
    while True:
        if importance[0] == max(importance):
            order += 1
            if document[0] == 'target':
                print(order)
                break
            else:
                importance.pop(0)
                document.pop(0)
        else:
            importance.append(importance.pop(0))
            document.append(document.pop(0))