n=int(input())
list=[]
for i in range(n):
    list.append(int(input()))

array=sorted(list,reverse=True) # 내림차순 정렬 하는 법!

for i in array: # 리스트 요소 하나씩 출력
    print(i,end=' ')