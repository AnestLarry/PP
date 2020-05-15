from typing import List

from DataStruct.linkedlist import LinkedList


class HashMap:
    def __init__(self, l=32):
        if l < 16:
            print("It is too low.")
        self.__l = l
        self.__size = 0
        self.__arr: List[LinkedList] = [LinkedList() for _ in range(l)]

    def __len__(self):
        return self.__size

    def put(self, key, value):
        if (self.__size + 1) / self.__l > 0.7:
            self.expand(self.__l * 2)
        h = hash(key)
        self.__arr[h & (self.__l - 1)].append([key, value])
        self.__size += 1

    def get(self, key):
        h = hash(key)
        cur = self.__arr[h & self.__l - 1]
        if not cur.is_empty():
            for i in cur.travel():
                if i[0] == key:
                    return i[1]
        raise ValueError("Key is not in HashMap.")

    def removeKey(self, key):
        h = hash(key)
        cur = self.__arr[h & self.__l - 1]
        if not cur.is_empty():
            index = 0
            for i in cur.travel():
                if i[0] == key:
                    self.__size -= 1
                    cur.pop(index)
                index += 1

    def print(self, sep=' -> ', end='\n'):
        for i in self.__arr:
            for j in i.travel():
                print(j[0], ":", j[1], end=sep)
            print("\b\b\b\b    \b\b\b\b", end="")
            if not i.is_empty():
                print(end=end)

    def expand(self, l):
        if l > self.__l:
            self.__l = l
            temp_arr: List[LinkedList] = [LinkedList() for _ in range(l)]
            def put(key, value):
                h = hash(key)
                temp_arr[h & (self.__l - 1)].append([key, value])
            for i, j in self.travel():
                put(i, j)
            self.__arr = temp_arr
        else:
            ValueError("l only allow plus.")

    def travel(self):
        for i in self.__arr:
            if not i.is_empty():
                for j in i.travel():
                    yield j[0], j[1]
