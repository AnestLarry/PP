from DataStruct.queue import Queue

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
