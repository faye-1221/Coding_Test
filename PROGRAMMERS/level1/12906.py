def solution(arr):
    stack = []
    for i in arr:
        if stack and i == stack[-1]:
            stack.pop()

        stack.append(i)
    return stack