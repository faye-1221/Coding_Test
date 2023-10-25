while True:
    try:
        n = int(input())
        result = '1'
        while True:
            if int(result) % n == 0:
                print(len(result))
                break
            result += '1'
    except:
        break