from DataStruct.queue import Queue,PriorityQueue

print("---- Queue test")
q = Queue()
try:
    q.Dequeue()
except LookupError:
    print("Pass")

print("---- Enqueue test")
q.Enqueue(1)
q.Enqueue(3)
q.Enqueue(5)
q.Enqueue(7)
q.Enqueue(9)
q.Enqueue(11)
q.Enqueue(12)
q.Enqueue(14)
q.Enqueue(19)
q.print()

print("---- Dequeue test")
for _ in range(5):
    print("%d" % (q.Dequeue(),))

print("----- queue length")
print(len(q))

print("---- Dequeue all")
while not q.is_empty():
    q.Dequeue()
print("--- end")

print("---- PriorityQueue test")
print("---- Enqueue test")

pq = PriorityQueue()
pq.Enqueue(2)
pq.Enqueue(5)
pq.Enqueue(1)
pq.Enqueue(10)
pq.Enqueue(0)
print("----- length")
print(len(pq))

print("----- print")
pq.print()

print("---- Dequeue test")
print(pq.Dequeue())
print(pq.Dequeue())
print(pq.Dequeue())
print(pq.Dequeue())
print(pq.Dequeue())