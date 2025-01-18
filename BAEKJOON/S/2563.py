from collections import Counter
N = int(input())
paper_length = 100

paper = [[0 for _ in range(paper_length)] for _ in range(paper_length)]
for _ in range(N):
    left, bottom = map(int, input().split())
    for i in range(left-1, left+9):
        for j in range(bottom-1, bottom+9):
            paper[i][j] = 1

result = 0
for p in paper:
    result += Counter(p)[1]
print(result)