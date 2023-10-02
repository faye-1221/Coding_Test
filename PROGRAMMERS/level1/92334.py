def solution(id_list, report, k):
    id_dict = {}
    for idx, i in enumerate(id_list):
        id_dict[i] = idx

    count = [[] for _ in range(len(id_list))] # 유저가 신고한 유저
    fire_count = [0 for _ in range(len(id_list))] # 신고된 횟수
    answer = [0 for _ in range(len(id_list))]
    
    for i in report:
        user, fire = i.split(' ')
         # 유저가 해당 유저를 신고하지 않았다면
        if fire not in count[id_dict[user]]:
            fire_count[id_dict[fire]] += 1 # 신고 횟수 적립
            count[id_dict[user]].append(fire) # 신고한 유저 적립
    
    id_dict = dict(map(reversed, id_dict.items()))
    for idx, fire_ct in enumerate(fire_count):
        if fire_ct >= k:
            for idx2, ct in enumerate(count):
                if id_dict[idx] in ct:
                    answer[idx2] += 1
    
    return answer