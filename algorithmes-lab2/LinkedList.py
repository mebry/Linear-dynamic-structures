class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, index):

        cur_node = self.head
        count = 0

        while cur_node.next != None:
            if index == 0:
                cur_node = self.head
                self.head = cur_node.next
                return

            elif count + 1 == index:
                the_node_to_remove = cur_node.next
                the_node_after_removed = the_node_to_remove.next
                cur_node.next=the_node_after_removed
                return

            count += 1
            cur_node = cur_node.next

    def display(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    def contains(self,key):  
       current_node=self.head  
       while current_node!=None:  
           if current_node.data==key:  
               return True  
           current_node=current_node.next  
       return False

    def sort(self):
        while True:
            i = 0
            cur_node = self.head
            while True:
                next_node = cur_node.next
                if next_node == None:
                    break
                if next_node.data < cur_node.data:
                    x = next_node.data, cur_node.data = cur_node.data, next_node.data
                    i += 1
                cur_node = next_node
            if i == 0:
                break
