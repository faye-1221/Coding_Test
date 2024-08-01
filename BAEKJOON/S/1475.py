import sys
input = sys.stdin.readline
N = list(map(int, input().strip('\n')))
l = [[] for _ in range(len(N))]

for n in N:
    for i in l:
        if n not in i:
            i.append(n)
            break
        


# 9999
# 69
# 69
# 2세트

# 122
# 12
# 2
# 2세트

# 12635
# 12645
# 1세트

# 888888
# 8
# 8
# 8
# 8
# 8
# -> 6세트