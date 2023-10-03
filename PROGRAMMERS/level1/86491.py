def solution(sizes):
    max_num = 0
    min_num = 0
    
    for s in sizes:
        max_s = max(s)
        min_s = min(s)
        
        max_num = max(max_num, max_s)
        min_num = max(min_num, min_s)

        
    return max_num * min_num