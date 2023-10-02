def solution(arr):
    small = min(arr)
    arr.remove(small)
    
    if not arr:
        return [-1]
    else:
        return arr