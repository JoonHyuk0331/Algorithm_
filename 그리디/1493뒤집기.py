# 0101000 붙어있는걸 어떻게 0 1 0 1 0 0 0 으로 떼어놓을까
# -> result = list(map(int, number))

#data=list(map(int,input())) 근데 꼭 안떼어도 됨
data=input()
changeCnt=0
if len(data)==1:
     print(0)
     exit()
for i in range(1,len(data)):
    if data[i]!=data[i-1]:
        changeCnt+=1
print((changeCnt+1)//2)
    
