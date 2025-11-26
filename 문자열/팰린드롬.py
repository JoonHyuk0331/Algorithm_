"""
https://www.acmicpc.net/problem/8892
"""
t=int(input())

def pal(s):
    return 1 if s==s[::-1] else 0


for kk in range(t):
    #print(f"testcase======{kk}")
    arr=[]
    n=int(input())
    for _ in range(n):
        arr.append(input())
    flag=0
    for i in range(n-1):
        if flag:
            break
        for j in range(i+1,n):
            #print("검사:"+ arr[i]+arr[j])
            #print("검사:" + arr[j] + arr[i])
            if flag:
                break
            if pal(arr[i]+arr[j]) :
                print(arr[i]+arr[j])
                flag=1
            elif pal(arr[j]+arr[i]):
                print(arr[j]+arr[i])
                flag=1
    if not flag:
        print(0)



