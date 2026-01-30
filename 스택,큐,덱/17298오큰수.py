n=int(input())
arr=list(map(int,input().split()))
ans=[-1]*n
stk=[]

#스택에 넣는게 인덱스일수도 있다
stk.append(0)
for i in range(1,n):
    while stk:#스택이 비어있지 않는동안 반복
        #print(stk)
        topNum=arr[stk[-1]]
        aa=arr[i]
        if topNum<aa: #스택의 맨 위 값보다 입력값이 더 크면
            ans[stk.pop()]=aa #결과값 갱신
        else:
            break
    stk.append(i)

print(*ans)

