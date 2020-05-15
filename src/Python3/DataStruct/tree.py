from DataStruct.queue import Queue
class BinaryTree:
    def __init__(self,v,left=None,right=None) -> None:
        self.value = v
        self.left = left
        self.right = right

    def preOrderTraversal(self):
        yield self.value
        if self.left:
            for i in self.left.preOrderTraversal():
                yield i
        if self.right:
            for i in self.right.preOrderTraversal():
                yield i
    
    def inOrderTraversal(self):
        if self.left:
            for i in self.left.inOrderTraversal():
                yield i
        yield self.value
        if self.right:
            for i in self.right.inOrderTraversal():
                yield i

    def postOrderTraversal(self):
        if self.left:
            for i in self.left.postOrderTraversal():
                yield i
        if self.right:
            for i in self.right.postOrderTraversal():
                yield i
        yield self.value
    
    def layerTraveral(self):
        tempq = Queue()
        cur = self
        while cur:
            if cur.left:
                tempq.Enqueue(cur.left)
            if cur.right:
                tempq.Enqueue(cur.right)
            yield cur.value
            if not tempq.is_empty():
                cur = tempq.Dequeue()
            else:
                cur = None

        
