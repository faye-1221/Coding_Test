from collections import Counter
def solution(array, n):
    counter = Counter(array)
    if n in array:
        return counter[n]
    else:
        return 0