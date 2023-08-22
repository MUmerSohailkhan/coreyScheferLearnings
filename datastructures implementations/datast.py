from collections import deque

cue=deque([1,2,3,4,5])
# cue.append([1,2,3,4,5])
print(cue)
cue.popleft()
cue.popleft()
print(cue)