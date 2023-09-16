def solution(s):
    answer = 0
    dic = {"(":")",
           "[":"]",
           "{":"}"}
    s_origin = s
    for i in range(len(s)):
        stack = []
        for j in s: 
            if not stack:
                stack.append(j)
            else:
                try:
                    if j == dic[stack[-1]]:
                        stack.pop()
                    else:
                        stack.append(j)
                except(KeyError):
                    stack.append(j)
        if not stack:
            answer += 1
        s = s_origin[i+1:] + s_origin[:i+1]
    return answer