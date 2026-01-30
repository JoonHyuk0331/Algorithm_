"""
permutations 알아야 풀 수 있는 문제

소수 판별 알고리즘 외워둬
"""
from itertools import permutations

def solution(numbers):
    cnt=0
    def isPrimeNumber(n):
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    n_list=[ n for n in numbers] # [1,2,3]
    per=[]
    for i in range(1,len(n_list)+1): #1~3
        per+=permutations(n_list,i)
    #print(per)
    per_list=[]
    for p in per:
        per_list.append(int(''.join(p)))
    per_set=set(per_list)
    #print(per_set)

    for per in per_set:
        if isPrimeNumber(per):
            cnt+=1

    return cnt

print(solution("011"))