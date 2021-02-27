INITIAL_CAPACITY = 50
class LinkedList:
    def __init__(self, key, value):
        self.head = None
        self.tail = None
        if key is not None and value is not None:
            self.addNode(key, value)

    def addNode(self, key, value):
        if key is not None and value is not None:
            if self.head is None and self.tail is None:
                self.head = self.tail = LinkedListNode(key, value)
            else:
                node = self.head
                prev = None
                # if Key already exists: Update the value of a node
                while node is not None and node.key != key:
                    prev = node
                    node = node.next
                if node == None:  # means key is not present in the LinkedList
                    self.tail.next = LinkedListNode(key, value)
                    self.tail = self.tail.next
                else:
                    node.value = value  # updating with current value

    def returnNodeValue(self,key):
        if key is not None:
            node = self.head
            while node != None and node.key != key:
                node = node.next
            if node == None:
                print("key not found")
                return None
            return node.value

    def deleteNode(self,key):
        if key is not None:
            node = self.head
            prev = None
            while node is not None and node.key != key:
                prev = node
                node = node.next
            if node is None:
                return None
            result = node.value
            prev.next = node.next
            return result

class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self):
        self.size = 0
        self.capacity = INITIAL_CAPACITY
        self.table = [None]*self.capacity

    def hash(self,key):
        hashVal = 0
        if key is not None:
            for i,v in enumerate(key):
                hashVal += (i+len(key))**ord(v)
            return hashVal%self.capacity

    def insert(self,key,value):
        index = self.hash(key)
        self.size += 1

        if self.table[index] is None:
            self.table[index] = LinkedList(key,value)
        else:
            self.table[index].addNode(key,value)

    def find(self,key):
        if key is not None:
            index = self.hash(key)
            if self.table[index] is None:
                print("key not found")
                return None
            linkedList = self.table[index]
            result = linkedList.returnNodeValue(key)
            if result is None:
                print("key not found")
                #return None
            return result


    def delete(self,key):
        if key is not None:
            index = self.hash(key)
            if self.table[index] == None:
                print("key not found")
                return None
            linkedList = self.table[index]
            result = linkedList.deleteNode(key)
            if result is None:
                print("Key not found")
            else:
                self.size -= 1
            return result


