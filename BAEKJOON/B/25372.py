n = int(input())

for i in range(n):
    password = input()
    if len(password) >= 6 and len(password) < 10:
        print("yes")
    else:
        print("no")