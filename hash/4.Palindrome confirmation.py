from collections import Counter
def Mysolution(s):
    answer = True
    count=1
    nH= Counter(s)
    for key in nH:
        if nH[key]%2 != 0:
            if(count ==  0):
                answer =False
            count = count - 1
    return answer     

def solution(s):
    sH = Counter(s)
    odd = 0
    for key in sH:
        if sH[key] % 2 ==1:
            odd +=1
    return odd<=1
                      
print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))
