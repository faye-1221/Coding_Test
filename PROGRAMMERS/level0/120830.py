def solution(n, k):
    ser = n//10
    k -= ser
    return (n*12000) + (k*2000)