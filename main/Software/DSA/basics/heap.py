import heapq

h = [6,1,0,0,4]
heapq.heapify(h)

print(h)
a = heapq.heappop(h)
print(a)
a += 10
print(h)
heapq.heappush(h, a)
print(h)