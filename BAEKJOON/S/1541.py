# import re
# N = re.split(r'([-, +])', input())
# print(N)

# stack = []
# result = 0
# i = 0

# while i != len(N):
    
#     if N[i].isdigit():
#         stack.append(N[i])
#     elif stack and N[i] == '+':
#         i+=1
#         result += (int(stack.pop())+int(N[i]))
#     i += 1

# for i in stack:
#     result -= int(i)

# print(result)

# 다른 코드 1
exp = input().split('-') # '-'를 기준으로 split해서 저장

num = []

for i in exp:
    result = 0
    tmp = i.split('+') # '+'를 기준으로 split

    for j in tmp:
        result += int(j)
    
    num.append(result)

n = num[0] # 식의 제일 처음은 숫자로 시작하므로 0번째 값에서 나머지 값들을 뺀다.

for i in range(1, len(num)):
    n -= num[i]
print(n)

# 다른 코드 2: 최초로 마이너스가 나오기 전까지 나오는 숫자는 모두 더해야 하므로, 이후 마이너스가 나오는 순간 그 뒤에 있는 모든 수를 뺀다.
arr = input().split('-')
s = 0
for i in arr[0].split('+'): # 리스트의 [0]은 최초 마이너스가 나오기 전의 값이므로 다 덧셈한다.
    s += int(i)

for i in arr[1:]: # 이제 모두 빼줘야 하는 숫자인데, '+'도 함께 있는 숫자도 있을것이다.
    for j in i.split('+'): # split을 해서 단독 숫자는 그냥 반환되고, '+'는 split하여 뺀다.
        s -= int(j)
print(s)