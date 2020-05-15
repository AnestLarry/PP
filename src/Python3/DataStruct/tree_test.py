from tree import BinaryTree

print("--------- generate data")
    #        1
    #      /   \
    #    2       3
    #  /   \    /  \
    # 4     5  6    7
    #  \
    #    9
print(r"""
           1
         /   \
       2       3
     /   \    /  \
    4     5  6    7
     \
       9
""")
bt = BinaryTree(1)
bt.left = BinaryTree(2)
bt.right = BinaryTree(3)
bt.left.left = BinaryTree(4)
bt.left.right = BinaryTree(5)
bt.right.left = BinaryTree(6)
bt.right.right = BinaryTree(7)
bt.left.left.right  = BinaryTree(9)

print("----- pre Order Traversal")
for i in bt.preOrderTraversal():
    print(i,end=' ')
print()

print("----- in Order Traversal")
for i in bt.inOrderTraversal():
    print(i,end=' ')
print()

print("----- post Order Traversal")
for i in bt.postOrderTraversal():
    print(i,end=' ')
print()

print("----- layer Traveral")
for i in bt.layerTraveral():
    print(i,end=' ')
print()