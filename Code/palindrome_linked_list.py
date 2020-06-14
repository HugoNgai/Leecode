#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        # 时间复杂度O(n), 空间复杂度O(1)
        if head is None:
            return True

        first_half_end = self.end_of_first_half(head)
        reversed_second_half = self.reverse_linked_list(first_half_end.next)

        first_half_position = head
        second_half_position = reversed_second_half

        while second_half_position:
            if first_half_position.val != second_half_position.val:
                return False
            first_half_position = first_half_position.next
            second_half_position = second_half_position.next

        return True

        # 时间复杂度O(n), 空间复杂度O(n)
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]

        # 递归 时间复杂度O(n), 空间复杂度O(n)
        self.front_pointer = head
        return self.recursively_check(head)

    def recursively_check(self, current_node):
        if current_node is not None:
            if not self.recursively_check(current_node.next):
                return False
            if self.front_pointer.val != current_node.val:
                return False
            self.front_pointer = self.front_pointer.next
        return True

    def end_of_first_half(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_linked_list(self, head):
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

