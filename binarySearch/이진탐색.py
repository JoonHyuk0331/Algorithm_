# https://www.acmicpc.net/workbook/view/8400
# 반복문으로 이진 탐색 구현하기
# 10 7 (10개의 항목에서 7을 찾겠다)
# 1 3 5 7 9 11 13 15 17 19
# 출력:4

# https://www.acmicpc.net/blog/view/109
# 이분탐색 읽어보면 좋은 글

def binarySearch(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid+1
        if arr[mid]<=target:
            start=mid+1
        else:
            end=mid-1

n,tg=map(int,input().split())
list=list(map(int,input().split()))
list.sort() # 주의 이분 탐색은 반! 드! 시! 정렬된 리스트에만 실행해야된다
print(binarySearch(list,tg,0,n-1))