#작은 문제부터 답을 도출하는 바텀업
d=[0]*100

d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]

print(d[n])