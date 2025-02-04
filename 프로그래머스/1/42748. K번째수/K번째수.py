def solution(array, commands):
    answer = []
    for comm in commands:
        i, j, k = comm[0], comm[1], comm[2]
        arr  = array[i-1:j]
        arr = sorted(arr)
        num = arr[k-1]
        answer.append(num)
    return answer