"""
https://www.acmicpc.net/problem/18406
"""

string=input()
length=len(string)
sum_left=0
sum_right=0

for i in range(length//2):
    sum_left+=int(string[i])
for i in range(length//2,length):
    sum_right += int(string[i])

if sum_left==sum_right:
    print("LUCKY")
else:
    print("READY")