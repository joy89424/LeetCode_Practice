# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 反轉鏈結
        r_list = ListNode()
        current = r_list
        stack = []
        i = 0
        # (1)將位置存進stack中
        while head:
            stack.append(head.val)
            head = head.next
            i += 1

        # (2)pop stack
        for j in range(i):
            current.next = ListNode(stack.pop())
            current = current.next

        # 回傳鏈結
        return r_list.next