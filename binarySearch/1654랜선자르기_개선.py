def isCut(lanList,needCnt,length):
    #print(f'isCut: {needCnt} 개 {length} 길이만큼 자를겁니다')
    cutCnt=0
    for lan in lanList:
        cutCnt+=lan//length
    if needCnt<=cutCnt:
        #print("oo자를수 있습니다oo")
        return True
    else:
        #print("xx자를수 없습니다xx")
        return False
    
def bs(target,lanList,needCnt): #큰거에서 작은거로 탐색
    result=0
    start=1
    end=target #1~802에서 이분탐색
    while start<=end:
        mid=(start+end)//2
        #print(f'bsLoop: {mid} 숫자로 나눌수 있는지 검사해봅니다')
        if isCut(lanList,needCnt,mid):# 401로 나눠보고 가능하면 더 큰 수로 잘라도 됨
            result=mid
            start=mid+1
        else: # 안잘리면 더 작은 수로 잘라야함
            end=mid-1
    return result

k,n=map(int,input().split()) #랜선의 개수, 필요한 랜선의 개수
lanList=sorted([int(input()) for _ in range(k)])

print(bs(lanList[-1],lanList,n)) #802부터 찾아주세요,lanList,n개로 잘라주세요

