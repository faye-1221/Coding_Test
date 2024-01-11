def solution(k, score):
    # 매일 score가 발표, 명예의 전당에 top k가 올라감
    # 명예의 전당에서의 최하위 점수를 return
    hall_list = []
    answer = []

    for s in score:
        if len(hall_list) == k: # 명예의 전당이 다 찼으면
            min_hall = min(hall_list)
            if min_hall < s: # 명예의 전당의 값보다 새로운 score가 크면
                hall_list[hall_list.index(min_hall)] = s
        else:
            hall_list.append(s)
        answer.append(min(hall_list))
    return answer

# 그냥 리스트에 먼저 추가하고 remove로 삭제하는 식으로 하심
# def solution(k, score):

#     q = []

#     answer = []
#     for s in score:

#         q.append(s)
#         if (len(q) > k):
#             q.remove(min(q))
#         answer.append(min(q))

#     return answer