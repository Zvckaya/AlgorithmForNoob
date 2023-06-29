def solution(score,k):
    answer = 0
    n = len(score)
    for i in range(n):
        if score[i]>=k:
            answer+=1
    return answer

print(solution([60,50,80,90,55,70,65,45],60))
print(solution([10,20,30,40,50],60))