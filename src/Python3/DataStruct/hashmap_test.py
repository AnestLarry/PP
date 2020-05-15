from DataStruct.hashmap import HashMap

hp = HashMap()

print("----------put test")
hp.put("0101", "John")
hp.put("0102", "Amy")
hp.put("0103", "Honey")

print("-------------len(3) and print")
print(len(hp))
hp.print()

print("----------get test")
print(hp.get("0101"))
print(hp.get("0103"))
print(hp.get("0102"))
print(hp.get("0101"))
print(hp.get("0102"))

print("----------travel test")
for i in hp.travel():
    print(i)
print("--------remove key")
hp.removeKey("0101")
hp.print()
print("1-----")
hp.removeKey("0102")
hp.print()
print("2-----")
hp.removeKey("0103")
hp.print()
print("3------")

print(len(hp))

print("------------auto expand it")
for i in range(0, 72, 2):
    hp.put(i, i ** 2)
print(len(hp))
hp.print()

print("------------try to error it")

hp.expand(1)
print(len(hp))