import ctypes
class DynamicArray(object):
    def __init__(self):
        self.count = 0
        self.capacity = 2
        self.data = self.make_array(self.capacity)

    def add(self, elem):
        if self.count == self.capacity:
            self.capacity = 2 * self.capacity
            self._resize(self.capacity)
        self.data[self.count] = elem
        self.count += 1

    def show(self):
        i = 0
        while i < self.count:
            print(self.data[i])
            i += 1

    def contains(self,elem): 
      for i in range(self.count): 
          if elem==self.data[i]: 
              return True 

      return False 

    def removeAt(self, index):
        if self.count == 0:
            return
        if index < 0 or index >= self.count:
            return IndexError("index out of the range")
        if index == self.count - 1:
            self.data[index] = 0
            self.count -= 1
            return
        for i in range(index, self.count - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.count - 1] = 0
        self.count -= 1

    def indexOf(self, elem):
        for i in range(self.count):
            if elem == self.data[i]:
                return i
        return -1

    def insert(self, item, index):
        if index < 0 or index > self.count:
            print("index out of the range")
            return
        if self.count == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.n - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]
        self.data[index + 1] = item
        self.count += 1

    def _resize(self, new_cap):
        new_arr = self.make_array(new_cap)
        for k in range(self.count):
            new_arr[k] = self.data[k]
        self.data = new_arr
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

 