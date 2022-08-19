while True:
    try:
        for _ in range(5):
            A, B = map(int, input().split(' '))
            print(A+B)
    except:
        break
