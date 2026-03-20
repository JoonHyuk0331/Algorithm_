n=int(input())

for i in range(n):
    str=input()
    stk=[]
    for s in str:
        # print(stk)
        if not stk:
            stk.append(s)
            continue

        if stk[-1]=='(' and s==')':
            stk.pop()
        else:
            stk.append(s)

    if stk:
        print("NO")
    else:
        print("YES")