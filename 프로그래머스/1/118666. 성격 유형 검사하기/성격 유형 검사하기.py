# survey에서 주어진 값들의 앞캐릭터는 비동의 관련, 뒤캐릭터는 동의 관련
# choice는 1~7 (매우 비동의 ~ 매우 동의)
# 지표 별로 동점이라면 사전 순으로 앞 알파벳을 선택
def solution(survey, choices):
    personality = {"R":0, "T":0,
                   "C":0, "F":0,
                   "J":0, "M":0,
                   "A":0, "N":0}
    
    for idx, category in enumerate(survey):
        first  = category[0]
        second = category[1]
        choice = choices[idx]
        
        if choice < 4:
            personality[first] += 4 - choice
        elif choice > 4: 
            personality[second] += choice - 4
        else:
            continue
            
    first_types = ['R', 'C', 'J', 'A']
    second_types = ['T', 'F', 'M', 'N']
    
    answer = ''.join(first if personality[first] >= personality[second] else second for first, second in zip(first_types, second_types))
    return answer