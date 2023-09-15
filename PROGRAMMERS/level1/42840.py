def solution(answers): 
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    scores=[0,0,0]
    answer = []

    for idx in range(len(answers)):
        if answers[idx]==one[(idx+1)%(len(one))-1]:
            scores[0]+=1
        if answers[idx]==two[(idx+1)%(len(two))-1]:
            scores[1]+=1
        if answers[idx]==three[(idx+1)%(len(three))-1]:
            scores[2]+=1
            
    max_score=max(scores)
    for score_idx in range(len(scores)):
        if scores[score_idx]==max_score:
            answer.append(score_idx+1)
    return answer