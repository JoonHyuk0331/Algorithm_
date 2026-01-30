import sys

string=list(sys.stdin.readline().strip())
word=list(sys.stdin.readline().strip())
listed_word=list(word)
stk=[]
word_nums=len(word)

for c in string:
    stk.append(c)
    while stk[-word_nums:]==listed_word:
        for _ in range(word_nums):
            stk.pop()

if stk:
    print("".join(map(str, stk)))
else:
    print("FRULA")