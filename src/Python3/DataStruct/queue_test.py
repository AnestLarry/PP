from DataStruct.queue import Queue

q = Queue()
try:
    q.pop()
except LookupError:
    print("Pass")

print("---- push test")
q.push(1)
q.push(3)
q.push(5)
q.push(7)
q.push(9)
q.push(11)
q.push(12)
q.push(14)
q.push(19)
q.print()

print("---- pop test")
for _ in range(5):
    print("%d" % (q.pop(),))

print("----- queue length")
print(len(q))

print("---- pop all")
while not q.is_empty():
    q.pop()
print("--- end")
