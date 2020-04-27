from DataStruct.stack import *

s = Stack()
print("---- push test")
s.push(1)
s.push(2)
s.push(1)
s.push(2)
s.push(1)
s.push(2)
s.print()

print("---- push test")
for i in range(10, 20):
    s.push(i)

print("---- pop test")
print("%d %d %d %d" % (s.pop(), s.pop(), s.pop(), s.pop()))

print("---- stack length test")
print(len(s))

print("---- pop all test")
while not s.is_empty():
    s.pop()

print("---- stack length test")
print(len(s))
