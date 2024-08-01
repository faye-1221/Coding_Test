def back(n, test):
    for i in range(6, len(test)+1):
        print(test[:i])
            

while True:
    testcase = list(map(int, input().split()))
    if testcase[0] == 0:
        break

    back(testcase[0], testcase[1:])

