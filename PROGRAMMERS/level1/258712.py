def solution(friends, gifts):
    answer = 0
    give_get = {}
    for friend in friends:
        give_get[friend] = [0, {}] # 선물지수, 누구한테 줬는지
        for friend2 in friends:
            if friend != friend2:
                give_get[friend][1][friend2] = 0
    
    for gift in gifts:
        give, get = gift.split()
        give_get[give][0] += 1
        give_get[give][1][get] += 1
        give_get[get][0] -= 1 
    
    for giver, info in give_get.items():
        get = 0
        for reciever, num in info[1].items():
            if giver == reciever: continue
            if num > give_get[reciever][1][giver]: 
                get += 1
            elif num == give_get[reciever][1][giver]:
                if give_get[giver][0] > give_get[reciever][0]:
                    get += 1
        answer = max(answer, get)
    return answer
        