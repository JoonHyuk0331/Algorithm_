from collections import deque

q=deque()

q.append(1)
q.append(2)
q.append(3)

print(q)
print(q[0]) #rear
print(q[-1]) #front

"""
Queue

rear              front
0                    -1
=======================
popleft          append 


"""