def solution(numbers):
    result = [i for i in range(0, 10)]
    
    for r in range(0, 10):
        if r in numbers:
            result.remove(r)
    return sum(result)