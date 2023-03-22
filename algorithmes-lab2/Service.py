from random import randint
from LinkedList import LinkedList
from DynamicArray import DynamicArray


def display_list(lst):
    cur_node = lst.head
    output = ""
    while cur_node != None:
            output += str(cur_node.data) + " "
            cur_node = cur_node.next
    print(output)    



def display_array(arr):
    i = 0
    output = ""
    while i < arr.countn:
        output += str(arr.data[i]) + " "
        i += 1
    print(output) 
           

def calculate_for_list(head,list2,list3,result_list):
    while head:
        if (not list2.contains(head.data)) and not list3.contains(head.data):
            result_list.add(head.data)
        head=head.next


def calculate_for_array(arr1,arr2,arr3,result_arr):
    for i in range(arr1.count): 
        if (not arr2.contains(arr1.data[i]) and not arr3.contains(arr1.data[i])):
            result_arr.add(arr1.data[i])
            

def unique_elements(list1,list2,list3):

    result_list=LinkedList()

    calculate_for_list(list1.head,list2,list3,result_list)
    calculate_for_list(list2.head,list1,list3,result_list)
    calculate_for_list(list3.head,list1,list2,result_list)
   
    return result_list



def unique_elements_for_arrays(arr1,arr2,arr3): 

   result_arr=DynamicArray() 

   calculate_for_array(arr1,arr2,arr3,result_arr) 
   calculate_for_array(arr2,arr1,arr3,result_arr) 
   calculate_for_array(arr3,arr1,arr2,result_arr) 

   return result_arr

def fill_list(count_elements, lst,min_value=-10,max_value=20):
    i = 0
    while(i < int(count_elements)):
        lst.add(randint(min_value, max_value))
        i += 1


#def unique_elements_for_arrays(arr1,arr2,arr3): 
#   result_arr=DynamicArray() 
    
#   for i in range(arr1.count): 
#      if (not arr2.contains(arr1.data[i])) and (not arr3.contains(arr1.data[i])): 
#          result_arr.append(arr1.data[i]) 
            
#   for i in range(arr2.count): 
#      if (not arr1.contains(arr2.data[i])) and (not arr3.contains(arr2.data[i])): 
#          result_arr.append(arr2.data[i]) 
            
#   for i in range(arr3.count): 
#      if (not arr1.contains(arr3.data[i])) and (not arr2.contains(arr3.data[i])):  
#          result_arr.append(arr3.data[i]) 
            
#   return result_arr 

#def unique_elements(list1,list2,list3):
#    result_list=LinkedList()
#    element_of_first_list=list1.head

#    while element_of_first_list:
#        if (not search(element_of_first_list.data,list2)) and (not search(element_of_first_list.data,list3)):
#            result_list.add(element_of_first_list.data)
#        element_of_first_list=element_of_first_list.next

#    element_of_second_list=list2.head

#    while element_of_second_list:
#        if (not search(element_of_second_list.data,list1)) and (not search(element_of_second_list.data,list3)):
#            result_list.add(element_of_second_list.data)
#        element_of_second_list=element_of_second_list.next

#    element_of_third_list=list3.head

#    while element_of_third_list:
#        if (not search(element_of_third_list.data,list1)) and (not search(element_of_third_list.data,list2)):
#            result_list.add(element_of_third_list.data)
#        element_of_third_list=element_of_third_list.next

#    return result_list

