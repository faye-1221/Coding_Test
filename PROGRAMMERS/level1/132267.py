def solution(a, b, n):
    result = 0
    while n >= a:
        div, mod = divmod(n, a)
        result += (div) * b
        n = mod + (div * b)
    return result