def solution(number, k):
    answer = []

    for num in number: # num 하나씩 돌기
        # k가 0보다 크고, answer에 값이 있고, answer 마지막 값보다 현재값이 크면
        while k > 0 and answer and answer[-1] < num:
            answer.pop() # answer 마지막을 빼고
            k-= 1 # k - 1
        answer.append(num) # answer에 저장

    return ''.join(answer[:len(answer)-k]) # k > 0 이상이면 스택에서 k개 삭제 후 join해서 결과 값 반환