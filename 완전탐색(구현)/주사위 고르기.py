from itertools import combinations,product
from bisect import bisect_left,bisect_right

def solution(dice):

    l=len(dice)
    a_combinations=list(combinations(dice,l//2))
    a_record = {}  # 특정 조합에서 승리 횟수 저장 승리 횟수는 유일하다

    for a_combination in a_combinations:
        b_combination=[d for d in dice if d not in a_combination]

        a_win_cnt=0
        number_of_cases=list(product(range(6),repeat=l//2)) # 주사위 경우의 수

        # A의 모든 합
        sum_of_a_list=[] # 특정 조합으로 골랐을때 나올수 있는 점수 합의 모든 경우의 수가 들어간 리스트
        for case in number_of_cases:
            sum_of_a=0
            for idx,a_dice_num_list in enumerate(a_combination):
                sum_of_a+=a_dice_num_list[case[idx]]

            sum_of_a_list.append(sum_of_a)
        #print(sum_of_a_list)

        sum_of_b_list=[]
        for case in number_of_cases:
            sum_of_b = 0
            for idx, b_dice_num_list in enumerate(b_combination):
                sum_of_b += b_dice_num_list[case[idx]]

            sum_of_b_list.append(sum_of_b)
        #print(sum_of_a_list)
        #print(sum_of_b_list)

        sum_of_b_list.sort()
        for a_sum in sum_of_a_list:
            a_win_cnt+=bisect_left(sum_of_b_list,a_sum) # a_sum보다 작은 b 점수 합 개수 반환
            #print(f'{a_sum}:{bisect_left(sum_of_b_list,a_sum)}')

        #print(f'a_record[{a_win_cnt}]={list(a_combination)}')
        a_record[a_win_cnt]=list(a_combination)

    #print(a_record)

    ans=a_record[max(a_record.keys())]
    return comb_to_idx(ans)

def comb_to_idx(comb):
    idx_list=[]
    for li in comb:
        for idx,d in enumerate(dice):
            if li==d:
                idx_list.append(idx+1)
                break
    return idx_list

dice=[[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
solution(dice)