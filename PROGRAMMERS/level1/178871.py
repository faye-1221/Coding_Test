def solution(players, callings):
    dic = {}
    for idx, player in enumerate(players):
        dic[player] = idx
        
    for call in callings:
        rank = dic[call]
        dic[call] -= 1
        dic[players[rank - 1]] += 1
        
        players[rank - 1], players[rank] = call,players[rank - 1] 
        
    return players