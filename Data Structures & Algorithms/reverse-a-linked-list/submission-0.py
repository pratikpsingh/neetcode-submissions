# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Solution 1:
        nums = []
        temp = head
        while temp:
            nums.append(temp.val)
            temp = temp.next
        
        head = ListNode()
        temp = head
        i = len(nums) - 1
        while i >= 0:
            temp.next = ListNode(nums[i])
            temp = temp.next
            i -= 1
        return head.next
            
        