"""
N개의 음이 아닌 정수
이 정수들의 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟넘버를 만드려고 한다.
numbers -> list (1 <= numbers <= 50, 자연수)
target -> int (1 <= target <= 1000, 자연수)
return -> 타겟 넘버를 만들 수 있는 경우의 수
"""

def dfs(numbers, target, idx, curr_sum):
    if len(numbers) == idx: # 모든 숫자를 다 사용 (종료 조건)
        return 1 if curr_sum == target else 0
    return dfs(numbers, target, idx+1, curr_sum + numbers[idx]) + dfs(numbers, target, idx+1, curr_sum - numbers[idx])

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)