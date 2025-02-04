def solution(n, lost, reserve):
    # 원래는 모두가 하나씩 가지고 있던 상태
    # 모든 학생(맨 앞과 맨 뒷번호 일지라도)이 앞과 뒤가 있는 상태로 만들기 위해
    uniform  = [1] * (n+2) # 앞뒤로 하나씩 더 추가, 0~(n+1)
    
    for i in reserve:
        uniform[i]+=1 # 여벌의 체육복을 가진 학생은 +1 -> 2
    for i in lost:
        uniform[i]-=1 # 체육복을 도난당한 학생은 -1 -> 0
    
    for i in range(1, n+1):
        if uniform[i-1] == 0 and uniform[i] == 2: # 앞 번호에 빌려줄 경우가 우선 됨
            uniform[i-1:i+1] = [1, 1]
        elif uniform[i] == 2 and uniform[i+1]==0:
            uniform[i:i+2] = [1,1]
        
    return len([x for x in uniform[1:-1] if x > 0])