# 카드 뭉치 2개 
# 카드 뭉치 중 순서는 마음대로지만 같은 카드 안에 있는 단어들의 순서는 바꿀 수 없다
# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없다
# 그러니까 카드 뭉치 내의 2번째 단어를 사용하려면 첫번째거를 무조건 사용해야한다. -> 앞에거 부터 써야된다 ; Queue

from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    for word in goal:
        if cards1 and cards1[0] == word:
            cards1.popleft()
        elif cards2 and cards2[0] == word:
            cards2.popleft()
        else:
            return "No"
    
    return "Yes"
            
    
    
    
   