S = input()
zero = 0
one = 0
first_word = S[0]

def func(s, zero, one):
    if s == '0':
        zero += 1
    else:
        one += 1
    return zero, one

zero, one = func(first_word, zero, one)

for s in S[1:]:
    if first_word != s:
        first_word = s
        zero, one = func(s, zero, one)

if one > zero:
    print(zero)
else:
    print(one)

# 다른 사람 답안
# s=input()
# cnt=0
# for i in range(len(s)-1):
#     if s[i]!=s[i+1]:
#         cnt+=1
# print((cnt+1)//2) # 변화횟수는 뒤집는 횟수에 1을 더한 후 2로 나눈 값이므로 (cnt+1)//2)를 구해서 출력