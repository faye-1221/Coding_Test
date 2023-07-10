import sys
N, M = map(int, sys.stdin.readline().split())
site = []
password = []
for i in range(N):
    s, p = sys.stdin.readline().split()
    site.append(s)
    password.append(p)

out = []
for i in range(M):
    search = sys.stdin.readline().rstrip()
    idx = site.index(search)
    out.append(password[idx])

for i in out:
    print(i)