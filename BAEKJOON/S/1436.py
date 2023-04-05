N = int(input())
number = 666
roop = 0

while (True):
    if ('666' in str(number)):
        roop += 1
    if roop == N:    
        print(number)
        break
    number += 1
