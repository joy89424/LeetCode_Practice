# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode()
        current.next = head
        # 判斷鏈結是否為空
        if current.next:
            current = current.next

        while current.next:
            if current.val == current.next.val: # 這一個節點跟下一個節點值相同
                if current.next.next != None:  # 下下一個節點不為空，表示還沒到尾端
                    current.next = current.next.next
                else: # 下下一個節點為空，表示還到尾端了
                    current.next = None
            else:
                current = current.next
        return head