"""
find를 개선할 알고리즘을 찾아야함
set은 찾기 연산이 O(n)임을 이용
"""

#접두어를 해시에 넣고 전화번호 리스트에서 비교
def solution(phone_book):
    answer = True
    nums_set = set()
    for item in phone_book:
        for i in range(1,len(item)):
            nums_set.add(item[:i])

    for item in phone_book:
        if item in nums_set:
            answer=False

    return answer

#전화번호 리스트를 해시에 넣고 접두어 리스트에서 비교
def solution2(phone_book):
    # 1.Hash map생성
    hash_map = {}
    for nums in phone_book:
        hash_map[nums] = 1

        # 2.접두어가 Hash map에 존재하는지 찾기
    for nums in phone_book:
        arr = ""
        for num in nums:
            arr += num

            # 3. 본인 자체일 경우는 제외
            if arr in hash_map and arr != nums:
                return False

    return True

#sort/loop 풀이
def solution3(phone_book):
    answer=True
    phone_book.sort() #정렬 필수!
    for i,j in zip(phone_book,phone_book[1:]): #(1,2,3,4) 를 (1,2) (2,3) (3,4) 해주는 스킬
        if j.startswith(i):
            answer=False
            break
    return answer