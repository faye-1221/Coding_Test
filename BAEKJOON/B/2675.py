T = int(input())

for _ in range(T):
    R, S = input().split()
    S = list(S)
    for i in range(int(len(S))):
        print(S[i]*int(R), end='')
    print()
