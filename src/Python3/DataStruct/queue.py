class Queue:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self, node=None):
        self.__front: Queue.Node = node
        self.__rear: Queue.Node = node
        self.__len: int = 0

    def __len__(self):
        return self.__len

    def is_empty(self):
        return self.__front is None

    def Enqueue(self, data):
        if self.__front is None:
            self.__front = self.rear = self.Node(data)
        else:
            self.__rear.next = self.Node(data,self.__rear)
            self.__rear = self.__rear.next
        self.__len += 1

    def Dequeue(self):
        if self.__front is None:
            raise LookupError("Empty Queue.")
        else:
            node = self.__front
            node.prev = None
            self.__front = node.next
            self.__len -=1
            return node

    def print(self,sep=' ',end="\n"):
        cur = self.__front
        while cur:
            print(cur.data,end=sep)
            cur = cur.next
        print(end=end)
