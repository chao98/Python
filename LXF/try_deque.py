from collections import deque

d = deque('ghi')
for elem in d:
    print(elem)

d = deque([], maxlen=5)
for i in range(10):
    d.append(i)

for elem in d:
    print(elem)

print(d)