from LinkedList import LinkedList


def search(key,lst):
    current_node = lst.head
    while current_node != None:
        if current_node.data==key:
            return True
        current_node = current_node.next
    return False

def calculate(head,list2,list3,resultList):
    while head:
        if (not search(head.data,list2)) and (not search(head.data,list3)):
            resultList.add(head.data)
        head=head.next

def unique_elements(list1,list2,list3):

    result_list=LinkedList()

    calculate(list1.head,list2,list3,result_list);

    calculate(list2.head,list1,list3,result_list);

    calculate(list3.head,list1,list2,result_list);
   
    return result_list


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

