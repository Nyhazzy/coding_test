"""
N개의 음이 아닌 정수
이 정수들의 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟넘버를 만드려고 한다.
numbers -> list (1 <= numbers <= 50, 자연수)
target -> int (1 <= target <= 1000, 자연수)
return -> 타겟 넘버를 만들 수 있는 경우의 수
"""
def solution(numbers, target):
    answer = 0
    
    leaves = [0]
    
    for num in numbers:
        temp = []
        
        for leaf in leaves:
            temp.append(leaf + num)
            temp.append(leaf - num)
        
        leaves = temp
        
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer