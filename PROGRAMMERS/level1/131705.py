from itertools import *
def solution(number):
    l = list(combinations(number, 3))
    result = 0
    for i in l:
        if sum(i) == 0:
            result += 1
    return result