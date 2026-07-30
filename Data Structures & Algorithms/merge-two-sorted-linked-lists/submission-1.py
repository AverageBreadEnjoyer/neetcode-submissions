# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Tip 1: When 1 linked list reaches the finish line (hits null), we know the other 
        #   nodes in the unfininished list are whats left of the new list were outputting

        # Tip 2: min of both lined list currs, when that gets a min advances.


        new_linked_list = ListNode()
        tail = new_linked_list


        while list1 != None and list2 != None: #ends when both lists reaches the finish line
            least = min(list1.val,list2.val)
            if least == list1.val:
                tail.next = list1
                list1 = list1.next #correct
                
            elif least == list2.val:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
                
        #what I missed: moving tail up to iterate through the new list


        if list1:
            tail.next = list1
        
        elif list2:
            tail.next = list2
               
            
                
        return new_linked_list.next


                
           




