from LinkedList import LinkedList
from Service import unique_elements


list1=LinkedList()
list2=LinkedList()
list3=LinkedList()

list1.add(1)
list1.add(2)
list2.add(3)
list2.add(4)
list3.add(5)
list3.add(6)
list3.add(1)
list3.add(1)

result=unique_elements(list1,list2,list3)
list3.display()

print("dsda")

list3.remove(1)
list3.remove(1)
list3.display()


