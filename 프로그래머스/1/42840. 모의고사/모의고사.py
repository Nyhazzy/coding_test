def solution(answers):
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    
    # 각 수포자들이 맞춘 답 개수 저장
    score = [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == supo1[i % len(supo1)]:
            score[0] += 1
        if answers[i] == supo2[i % len(supo2)]:
            score[1] += 1
        if answers[i] == supo3[i % len(supo3)]:
            score[2] += 1
            
    result = [i+1 for i, s in enumerate(score) if s == max(score)]
    
    return result