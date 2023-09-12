import heapq
a = [54, 88, 7, 26, 93, 17, 49, 10, 11, 31, 22, 44, 20]
print('정렬 전:\t', a)

heapq.heapify(a)
print('힙:\t', a)

s=[]
while a:
    s.append(heapq.heappop(a))

print('정렬 후:\t', s)
