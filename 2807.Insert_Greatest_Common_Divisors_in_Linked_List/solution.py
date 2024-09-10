# coding=utf-8
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def greatest_common_divisors(first_number: int, second_number: int) -> int:
        for i in range(min(first_number, second_number), 1, -1):
            if first_number % i == 0 and second_number % i == 0:
                return i
        return 1

    def insertGreatestCommonDivisors(
            self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        head.next = ListNode(
            val=self.greatest_common_divisors(head.val, head.next.val),
            next=self.insertGreatestCommonDivisors(head.next)
        )
        return head
