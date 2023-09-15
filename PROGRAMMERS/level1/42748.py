def solution(array, commands):
    result = []
    for i in commands:
        arr = sorted(array[i[0]-1 : i[1]])
        result.append(arr[i[2]-1])        
    return result