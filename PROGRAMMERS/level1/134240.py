def solution(food):
    answer = ''
    for i in range(1, len(food)):
        food[i] = food[i]//2
        answer += str(i) * food[i]
    answer_copy = answer
    answer += '0'
    
    return answer + answer_copy[::-1]