# 종료 조건을 설정하는게 빡쎘음

n=int(input())
arr=list(map(int,input().split()))

stk=[]
target=1
for i in arr:
    if i==target: #타겟이 맞는지 찾아보고
        target+=1
        #매번 스택 활용이 가능한지 찾아본다
        while stk and stk[-1]==target:
            target+=1
            stk.pop()
    else:
        stk.append(i)

#print(target,n)
if not stk: #결론적으로 스택이 비어있다면
    print("Nice")
else:
    print("Sad")