from collections import Counter
def Mysolution(s):
    answer =0 
    odd = 0
    nH = Counter(s)
    for key in nH:
        if(nH[key]%2==1):
            if(odd!=0):
                nH[key]= nH[key]-1
            else:
                odd +=1
    for key in nH:
        answer = answer + nH[key]
    return  answer

def solution(s):
    sH=Counter(s)
    odd = 0
    for key in sH:
        if sH[key] %2==1:
            odd += 1
    return len(s) - odd + 1 if odd>0 else len(s)
    
                   
print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))
