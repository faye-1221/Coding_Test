k = int(input())

def recur(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n%2: # 짝수일 때
        return 1 - recur(n//2)
    else: # 홀수일 때
        return recur(n//2)
print(recur(k-1))

# print(bin( int(input()) -1 ).count('1')%2)
