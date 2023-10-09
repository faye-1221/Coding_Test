def solution(numbers, target):
    answer = 0
    
    
    def fun(idx=0, sum=0):
        nonlocal answer
        
        if idx == len(numbers):
            if sum == target:
                answer += 1
            return
            
        fun(idx+1, sum+numbers[idx])
        fun(idx+1, sum-numbers[idx])

        return answer

    return fun()