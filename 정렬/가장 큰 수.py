"""
https://school.programmers.co.kr/learn/courses/30/lessons/42746

1. 문자열 비교는 사전순
2. ''.join() : iterable의 요소들을 하나의 문자열로 합쳐줍
3. 문자열 곱하기

4. 문자열 자체를 늘려서 비교하지 말고 비교 시에만 일시적으로 늘리는 방법으로 가자

"""

def solution(numbers):
    #numbers의 원소들을 str형으로 변형하자
    num_list=list(map(str,numbers))

    #사전순 정렬
    num_list=sorted(num_list,key=lambda x:x*3, reverse=True)

    #iterable의 요소들을 하나의 문자열로 합쳐줍
    answer=''.join(num_list)

    return answer

print(solution([3, 30, 34, 5, 9]))