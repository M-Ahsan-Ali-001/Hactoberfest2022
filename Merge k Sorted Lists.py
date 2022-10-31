/*
Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6 
*/

class Solution:
    def mergeLists(self, head1, head2):
        head = ListNode(None)
        dummy = head
    
        while head1 and head2:
            if head1.val <= head2.val:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next

            dummy = dummy.next
    
        if head1:
            dummy.next = head1
        if head2:
            dummy.next = head2
        
        return head.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(None)
        
        for lst in lists:
            head.next = self.mergeLists(head.next, lst)
            
        return head.next
