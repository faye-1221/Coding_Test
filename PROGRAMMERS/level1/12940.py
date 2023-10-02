import math
def solution(n, m):
    result = [0, 0]
    result[0] = math.gcd(n, m)
    result[1] = n*m/result[0]
    
    return result