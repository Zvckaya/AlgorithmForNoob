def solution(sticks):
    answer = 1
    max = sticks[-1]
    n = len(sticks)
    for i in range(n-15-1),-1:
        if sticks[i]>max:
            answer+1
            max = sticks[i]
    return answer


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(solution(arr))