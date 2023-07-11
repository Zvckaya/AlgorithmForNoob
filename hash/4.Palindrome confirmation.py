from collections import Counter
def solution(s):
    answer = True
    count=1
    nH= Counter(s)
    for key in nH:
        if nH[key]%2 != 0:
            if(count ==  0):
                answer =False
            count = count - 1
    return answer     
                      
print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))
