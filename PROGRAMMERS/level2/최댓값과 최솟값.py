s = "-1 -2 -3 -4"
l = list(map(int, s.split()))
f1 = max(l)
f2 = min(l)

answer = str(f2) + " " + str(f1)
print(answer)
