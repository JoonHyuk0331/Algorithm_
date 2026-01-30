from collections import deque
from collections import Counter
n=int(input())
word_list=[] #
vis=[0]*(n+1)
for _ in range(n):
    word_list.append(input())

for i in range(n):
    #print(f'=={word_list[i]}==')
    if vis[i]:
        continue
    q=deque(word_list[i])
    word_len=len(word_list[i])
    for _ in range(word_len):
        q.append(q.popleft())
        new_word="".join(q)
        for idx in range(len(word_list)):
            #print(f"{new_word} vs {word_list[idx]}",end="")
            if word_list[idx]==new_word:
                #print("<-- correct")
                vis[idx]=1
            #print("")
    vis[i]=0

print(Counter(vis)[0]-1)

