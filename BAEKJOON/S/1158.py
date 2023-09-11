n, k = map(int, input().split())
l = [x for x in range(1, n+1)]


answer = []
num = 0

for t in range(n):
    num += k-1  
    if num >= len(l):
        num = num%len(l)
 
    answer.append(str(l.pop(num)))
print("<",", ".join(answer)[:],">", sep='')