T = int(input())
for i in range(T):
    n = int(input())
    bin_i = list(str(bin(n)))[::-1]

    result_l = []
    for idx, j in enumerate(bin_i[:-2]):
        if j == '1':
            print(idx, end=' ')
    print()
    
    
