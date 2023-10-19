while True:
    n, m = map(int, input().split())
    if not n and not m:
        break
    
    if n%m == 0:
        print("multiple")
    elif m%n == 0:
        print("factor")
    else:
        print("neither")
