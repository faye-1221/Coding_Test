def solution(s, n):
    answer = ''
    for alpha in s:
        
        if alpha == " ":
            answer += " "
        elif alpha.islower():
            answer += chr((ord(alpha)-ord('a')+n) % 26 + ord('a'))
        elif alpha.isupper():
            answer += chr((ord(alpha)-ord('A')+n) % 26 + ord('A'))
    
    return answer