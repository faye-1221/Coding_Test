N = int(input())
l = []
for _ in range(N):
    name, what = map(str, input().split())
    if what == 'enter':
        l.append(name)
    else:
        l.remove(name)

l = sorted(l, reverse=True)
for i in l:
    print(i)

# 다른 사람 풀이 - 해시
import sys
input = sys.stdin.readline

N = int(input())
company = {}
for _ in range(N):
    man, state = input().rstrip().split()
    if state == 'enter':
        company[man] = True
    else:
        del company[man]

print("\n".join(sorted(company.keys(), reverse=True)))