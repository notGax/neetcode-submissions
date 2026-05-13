# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head

        while curr is not None:
            next_node=curr.next # save the next node before changing the link
            curr.next=prev # reverse the link, now curr points backward
            prev=curr   # move prev forward to current node
            curr=next_node # move curr forward to the saved next node
        return prev