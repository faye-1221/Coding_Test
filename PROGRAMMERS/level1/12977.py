from itertools import combinations
def solution(nums):
    result = 0
    nCr = list(combinations(nums, 3))
    
    for n in nCr:
        if function(sum(n)):
            result += 1
    return result
    
def function(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True