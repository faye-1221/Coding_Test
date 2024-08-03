group = {}
N, M = map(int, input().split())
for _ in range(N): # 총 입력 받을 걸그룹의 수
    group_name = input()
    group_member_c = int(input())
    group_member = []
    for _ in range (group_member_c):
        group_member.append(input())
    group_member = sorted(group_member)
    group[group_name] = group_member

for _ in range(int(M)): # 퀴즈
    one = input() # 팀의 이름이나 멤버의 이름
    two = int(input()) # 퀴즈의 종류 0 또는 1: 0일 경우 팀의 이름 1일 경우 멤버의 이름

    # 0일 경우 멤버의 이름을 사전순으로 한줄에 한명
    # 1일 경우 해당 팀의 이름
    if two == 0:
        print(*group[one], sep='\n')
    else:
        print(*[k for k, v in group.items() if one in v])