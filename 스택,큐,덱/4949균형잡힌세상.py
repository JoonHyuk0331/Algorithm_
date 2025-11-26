#입력의 종료조건으로 마지막 . 가 들어오는 경우
#stk[-1] 검사 시 빈 배열일 수도 있다는 점을 유념해야함

while True:
    a=input()
    stk=[]
    #print("------",a,"-------")
    if a==".":
        break
    for i in a:
        if i in ["[","("]:
            stk.append(i)
        if i in ["]",")"]:
            if not stk:
                stk.append(i)
            if i=="]" and stk[-1]=="[":
                stk.pop()
            elif i==")" and stk[-1]=="(":
                stk.pop()
            else:
                stk.append(i)
        #print(stk)

    if stk: #리스트가 비어있지 않다면 no
        print("no")
    else:
        print("yes")


