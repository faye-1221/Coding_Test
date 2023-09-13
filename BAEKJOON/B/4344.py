c = int(input())
for i in range(c):
    n_score = list(map(int, input().split()))

    avg = sum(n_score[1:]) / n_score[0]
    
    cnt = 0
    for s in n_score[1:]:
        if s > avg:
            cnt += 1
        
    rate = cnt/n_score[0] * 100
    print(f'{rate:.3f}%')