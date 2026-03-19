k,m=map(int,input().split())

LANs=[int(input()) for _ in range(k)]

def cuttable(length): #length만큼 잘랐을때 m개만큼 잘리는지
    cnt=0
    for lan in LANs:
        cnt+=lan//length
    if m<=cnt:
        return True
    else:
        return False

st,en=1,max(LANs)
while st<=en:
    mid=(st+en)//2
    if cuttable(mid): # (TTFFFFF)에서 최대 T 인덱스 찾기
        st=mid+1
    else:
        en=mid-1
print(en)


