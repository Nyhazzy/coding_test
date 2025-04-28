# terms ["약관종류 유효기간", ... ] -> 딕셔너리로 바꾸기
# privacies ["개인정보수집일자 약관종류", ...]
# 약관의 유효기간은 몇 달로 주어지기 때문에 일에는 변화 없음. (일은 하루만 줄여주면 됨.)
# 그러면 수집한 날짜가 1일이면 유효기간에서 28일로 바꿔주긴해야하잖아?

def solution(today, terms, privacies):
    
    terms_dict = {}
    for term in terms:
        kind, month = term.split(" ")
        terms_dict[kind] = int(month)
    
    today_year, today_month, today_day = map(int, today.split("."))
    answer = [] # 파기해야할 개인정보의 인덱스 번호
    for idx, privacy in enumerate(privacies):
        collection_date, kind = privacy.split(" ")
        
        year, month, day = map(int, collection_date.split("."))
        
        # 수집 시작일자의 월에 유효기간 더하기 
        ex_month = month + terms_dict[kind]
        ex_year = year
        # 이렇게 하면 만약에 2024.07.01 에 수집했고 유효기간이 6달일 때, 만료기간이 2025.01.01이 아니라 2025.12.28 임. 이런건 어떻게 표현? 너무 케이스가 많아진다.
        if ex_month > 12:
            ex_year += (ex_month-1)//12
            ex_month = (ex_month-1) % 12 +1
            
        
        ex_day = day - 1
        if ex_day == 0:
            ex_day = 28
            ex_month -= 1
            if ex_month == 0:
                ex_month = 12
                ex_year -= 1
                
        if (ex_year, ex_month, ex_day) < (today_year, today_month, today_day):
            answer.append(idx+1)
        
            
    
    return answer