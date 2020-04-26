from linkedlist import *       

root = LinkedList()

print("---- insert test")
root.insert(2) 
root.insert(5)
root.insert(1, 0)
root.insert(3, -2)
root.insert(4, 3) 
root.insert(6, -1)
root.insert(0, 0)
root.print()
print("---- append test")
for i in range(7, 10):
    root.append(i)
root.print()

print("---- pop first and last") 
print(root.pop(0), "and", root.pop(), "popped.")
root.print()

print("---- pop after first and befor last")
print(root.pop(1), "and", root.pop(-2), "popped.")
root.print()

print("---- pop all")
for i in range(len(root)):
    root.pop()
print("chain length:",len(root))
