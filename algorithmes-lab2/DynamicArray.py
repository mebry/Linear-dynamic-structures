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

    def contains(self,elem): 
      for i in range(self.count): 
          if elem==self.data[i]: 
              return True 

      return False 
    
    def remove(self, elem):
        for i in range(self.count):
            if self.data[i] == elem:
                self.data[i] = self.data[self.count - 1]
                self.count -= 1
                break

    def remove_by_id(self, index):
        if 0 <= index < self.count:
            self.data[index] = self.data[self.count - 1]
            self.count -= 1

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

    def sort(self): 
        self.quick_sort(self.data,0,self.count-1) 

    def quick_sort(self,arr,start,end):
        if start>=end:
            return
    
        pivot_index=start
        left=start+1
        right=end
    
        while right>=left:
        
            if arr[left]>arr[pivot_index] and arr[right]<arr[pivot_index]:
                arr[left],arr[right]=arr[right],arr[left]
            
            if arr[left]<=arr[pivot_index]:
                left+=1
            
            if arr[right]>=arr[pivot_index]:
                right-=1
            
        arr[pivot_index],arr[right]=arr[right],arr[pivot_index]
    
        self.quick_sort(arr,start,right-1)
    
        self.quick_sort(arr,right+1,end)

 