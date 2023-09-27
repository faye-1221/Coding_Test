ss = input().split('.')
sol_str = ''

for x in ss:
    if len(x) % 2 == 1:
        print(-1)
        break

    while len(x) >= 4:
        sol_str+='AAAA'
        x = x[4:] # 4개를 AAAA로 변경했기 때문에 해당 부분을 삭제

    if len(x) == 2:
        sol_str+='BB'
        x = x[2:] # 2개를 BB로 변경했기 때문에 해당 부분을 삭제

    sol_str+='.'
else: # for문이 끝나면 어떻게 출력할지 인데 for 문 안에 break가 실행되면 else는 실행되지 않음.
    print(sol_str[:-1])