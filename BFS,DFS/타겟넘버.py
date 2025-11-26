def solution(numbers, target):
    max_depth=len(numbers)-1
    cnt=0
    def dfs(v,depth):
        nonlocal cnt
        if depth==max_depth:
            if v==target:
                cnt+=1
                return 0
            else:
                return 0
        dfs(v+numbers[depth],depth+1)
        dfs(v-numbers[depth],depth+1)
        return 0

    dfs(0,-1)
    return cnt

# 큐를 쓰지 않는 풀이법이 있음
def solution2(numbers, target):
    leaves = [0]  # 현재 레벨의 모든 노드

    for num in numbers:
        temp = []  # 다음 레벨의 모든 노드

        for leaf in leaves:
            temp.append(leaf + num)
            temp.append(leaf - num)

        leaves = temp  # 다음 레벨로 이동

    # 마지막 레벨에서 target과 같은 개수 세기
    count = 0
    for leaf in leaves:
        if leaf == target:
            count += 1

    return count

print(solution([4, 1, 2, 1],2))