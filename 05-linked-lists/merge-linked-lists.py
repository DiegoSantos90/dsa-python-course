'''
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to print a list (assuming it's already defined)
def print_list(node: Optional[ListNode], name: str):
    """Helper function to print a linked list in a readable format."""
    print(f"{name}: ", end="")
    if not node:
        print("NULL")
        return

    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result) + " -> NULL")

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        if not list1:
            return list2

        if not list2:
            return list1

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next

if __name__ == "__main__":
    # Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
    list_1 = ListNode(1, ListNode(2, ListNode(4)))
    list_2 = ListNode(1, ListNode(3, ListNode(4)))

    solution = Solution()

    print("--- Merging Linked Lists ---\n")
    merged_list = solution.mergeTwoLists(list_1, list_2)

    print("\n--- Merging Complete ---")
    print_list(merged_list, "Merged List")

