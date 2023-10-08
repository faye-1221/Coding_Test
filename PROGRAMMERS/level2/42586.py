import math
def solution(progresses, speeds):
    answer = []
    stack = []
    hun = 100
    for pro, speed in zip(progresses, speeds):
        A = math.ceil((hun-pro)/speed)
        if stack and A > stack[0]:
            answer.append(len(stack))
            stack = []
        stack.append(A)

    if stack:
        answer.append(len(stack))
        
    return answer