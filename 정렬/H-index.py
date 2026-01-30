

def solution(citations):
    answer = 0
    numbers=sorted(citations) # 1 3 5 7 9
    size=len(numbers)
    h_index=0
    for h in range(numbers[-1]+1): #0~9
        print(f'==={h}===')
        for i in range(size):
            print(f'{h} vs {numbers[i]}')
            if h<=numbers[i]:
                print(f'{h} <= {numbers[i]}')
                h_index=max(h_index,h)
                print(h_index)
                break

    print(h_index)
    return answer

solution([3, 0, 6, 1, 5])
"""
9 7 5 3 1
1 2 3 4 5 h인용
h <= h인용 이면서 h가 최대값
1 5 1
2 5
3 4 3 
4 4   vvvv
5 3 5 
6 3
7 2 7
8 2
9 1 9

9 1 9
8 2
7 2 7
6 3
5 3 5
4 4
3 4 3
2 5
1 5 1

111 11 5 1

1 5 11 111
h <= h인용 이면서 h가 최대값
1 4 1
2 4
3 4
4 4 vvvv
5 3 5
6 3
...
11 2 11
...
111 1 111


[3, 0, 6, 1, 5]
6 5 3 1 0

0 5 0
1 4 1
2 4
3 3 3 vvvv
4 2
5 2 5
6 1 6

"""