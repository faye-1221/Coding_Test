K, L = map(int, input().split())
dic = {}

for _ in range(L):
    number = input()
    
    if number in dic:
        del dic[number]
    dic[number]  = True

dic = list(dic.keys())[:K]
print(*dic, sep='\n')