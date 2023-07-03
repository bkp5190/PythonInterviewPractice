# Definition for singly-linked list.
from math import ceil
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        counter = 0
        while(current_node is not None):
            counter += 1
            current_node = current_node.next

        mid = ceil(counter / 2)
        if counter % 2 == 0:
            mid += 1
        current_node = head
        for _ in range(mid-1):
            current_node = current_node.next
        return current_node