from collections import defaultdict
def solution(clothes):
    hash_set=defaultdict(int)
    for item in clothes:
        category=item[1]
        hash_set[category]+=1

    ans=1
    for value in hash_set.values():
        ans*=(value+1)

    return ans-1

clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)