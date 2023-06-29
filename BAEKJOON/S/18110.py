import sys
def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    if not n:
        print(0)
    else:
        diff = [int(sys.stdin.readline()) for _ in range(n)]
        diff.sort()
        exc = my_round(n*0.15)

        if exc != 0:
            diff = diff[exc:-exc]
        cnt = n - 2 * exc
        result = sum(diff)
        print(my_round(result/cnt))