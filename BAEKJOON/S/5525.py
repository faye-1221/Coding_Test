# 50점
# N = int(input())
# S_len = int(input())
# S = input()

# # S에 P_N이 몇 군데 포함되어 있는지
# NN = "IOI" + ("OI" * (N-1))
# NN_len = len(NN)

# result = 0

# for i in range(S_len):
#     if S[i:(i+NN_len)] == NN:
#         result += 1
# print(result)

# 100점
# P_N은 o가 N개...
N = int(input())
S_len = int(input())
S = input()

answer, i, count = 0, 0, 0

while i < (S_len-1):
    if S[i:i+3] == "IOI":
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -=1
    else:
        i += 1
        count = 0
print(answer)