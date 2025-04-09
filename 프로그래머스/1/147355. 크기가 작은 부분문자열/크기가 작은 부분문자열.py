def solution(t, p):
    len_p = len(p)
    len_t = len(t)
    end = len(t) - len(p) + 1
    
    num_p = int(p)
    answer = 0
    
    for i in range(end):
        cur_t = t[i:i+len_p]
        num_cur_t = int(cur_t)
        if num_cur_t <= num_p:
            answer += 1    
    
    
    return answer