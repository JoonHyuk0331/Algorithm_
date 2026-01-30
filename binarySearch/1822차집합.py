n1,n2=map(int,input().split())
arrA=list(map(int,input().split()))
arrB=list(map(int,input().split()))

setA=set(arrA)
setB=set(arrB)

differenceSet=sorted(setA-setB)

print(len(differenceSet))
print(' '.join(map(str,differenceSet)))