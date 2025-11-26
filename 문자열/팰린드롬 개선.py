"""
https://www.acmicpc.net/problem/8892
"""
t=int(input())

def palindrome():
    n = int(input())
    arr=[input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                word = arr[i] + arr[j]
                if word == word[::-1]:
                    return word
    return 0

while t > 0:
    ans = palindrome()
    print(0) if ans == 0 else print(ans)
    t -= 1



