def solution(coin, cards):
    n=len(cards)
    valid_cards=[0]*15

    def n_possible(target_n):
        for idx in range(1,15):
            print(f'{idx}와{target_n - idx} 비교')
            if idx==target_n-idx:
                continue
            if valid_cards[idx] and valid_cards[target_n-idx]:
                valid_cards[idx]=0
                valid_cards[target_n-idx]=0
                print(f'{idx}와{target_n-idx}의 합이{target_n}입니다')
                return 1
        return 0

    for i in range(n//3):
        valid_cards[cards[i]]=1

    loop=0
    for i in range((n//3),n,2): #[3, 6, 7, 2 / 1, 10, 5, 9 / 8, 12, 11, 4]
        loop+=1
        print(f'{loop}:번째루프=================')
        print(valid_cards)
        if n_possible(n+1):
            print("기존 성공")
            continue
        else:
            print("기존 실패")
            print(valid_cards)
            if coin:
                coin-=1
            else:
                break
            valid_cards[cards[i]]=1
        if n_possible(n+1):
            print("앞에꺼 추가해서 성공")
            continue
        else:
            print("앞에꺼 추가해도 실패")
            print(valid_cards)
            coin += 1
            valid_cards[cards[i]]=0
            coin -= 1
            valid_cards[cards[i+1]]=1
        if n_possible(n+1):
            print("뒤에꺼 추가해서 성공")
            continue
        else:
            print("뒤에꺼 추가해도 실패")
            print(valid_cards)
            if coin:
                coin -= 1
            else:
                break
            valid_cards[cards[i]]=1
            valid_cards[cards[i+1]]=1
        if n_possible(n+1):
            print("둘다 추가해서 성공")
            continue
        else:
            print("둘다 추가해도 실패")
            print(valid_cards)
            break
    print(loop)


solution(4,[3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4])

#500(뽑아서비교)x4(뽑는경우의수)=2000 개의 리스트에 대하여 n으로 짝지어지는게 있는지 확인
# 1->999가 있는가? 2->988이 있는가?
