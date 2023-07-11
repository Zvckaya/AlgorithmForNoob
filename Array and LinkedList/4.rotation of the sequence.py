from collections import deque

def solution(nums,k):
    answer = deque(nums)
    for i in range(k):
        answer.append(answer.popleft())
    return list(answer)


print(solution([3,7,1,5,9,2,8],3))