import ctypes
class DynamicArray():

    def __int__(self):
        self.length = 0
        self.capacity = 1
        self.Array = self._make_new_array(self.capacity)

    def _make_new_array(self,capacity:'int'):
        return (capacity*ctypes.py_object)()


    """
    length of an array list
    """
    def __len__(self):
        return self.length

    """
    append at the end of an array
    """
    def append(self,val:'int'):
        if self.length == self.capacity:
            self.resize(2*self.capacity)
        self.Array[self.length] = val
        self.length += 1
        return self.Array


    """
    insertAt particular index
    """
    def insertAt(self,index:'int',val:'int'):
        if not 0<=index<self.length:
            print("index out of bounds")
            return
        if self.length == self.capacity:
            self.resize(2*self.capacity)

        for i in range(self.length-1,index-1,-1):
            self.Array[i+1] = self.Array[i]
        self.Array[index] = val
        self.length += 1
        return self.Array

    """
    delete from the last position
    """
    def delete(self):
        if self.length == 0:
            print("Array list is empty")
            return
        self.Array[self.length-1] = 0
        self.length -= 1
        return self.Array

    """
    delete from particular index
    """
    def removeAt(self,index:'int'):
        if not 0<=index<self.length:
            print("index out of bound")
            return
        if index == self.length-1:
            self.delete()
            return self.Array
        for i in range(index,self.length-1):
            self.Array[i+1] = self.Array[i]
        self.length -=1
        return self.Array


    """
    resize
    """
    def resize(self,newCap):
        B = self._make_new_array(newCap)
        for i in range(self.length):
            B[i] = self.Array[i]
        self.Array = B


arrayList = DynamicArray()
print(arrayList.capacity)







