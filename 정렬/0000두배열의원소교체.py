n,k=map(int,input().split())
arr1=[]
arr2=[]
arr1=sorted(list(map(int,input().split())),reverse=False) # 1 2 3 4 5
arr2=sorted(list(map(int,input().split())),reverse=True) # 6 6 5 5 5
for i in range(k):
    if arr1[i]<arr2[i]:
        arr1[i],arr2[i]=arr2[i],arr1[i] #swap
    else:
        break
    
sum=0
for i in range(n):
    sum+=arr1[i]

print(sum)