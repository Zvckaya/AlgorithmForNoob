def solution(nums):
    answer = 0
    minN = 1000000000
    n = len(nums)
    for i in range(n):
        if nums[i] < minN:
            minN = nums[i]
            answer = i
    return answer

print("position of Min on Array =",solution([7,10,5,3,2,15,19]))