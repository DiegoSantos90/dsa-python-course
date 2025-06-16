'''
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
from typing import Optional

# Definition for singly-linked list (assuming it's already defined)
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
    # Create the linked list: 1 -> 2 -> 3
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head # Crio 2 ponteiros
        while curr:
            temp = curr.next    # temp guarda o next do nó corrente.
            curr.next = prev    # next do nó corrente recebe prev.
            prev = curr         # prev recebe o nó corrente.
            curr = temp         # nó corrente passa a ser o próximo nó a ser iterado.
        return prev

    # Create the linked list: 1 -> 2 -> 3
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # Base case head == None ou head.next == None
            return head

        new_head = self.reverseListRecursive(head.next) # Chama recursion utilization o próximo nó
        head.next.next = head
        head.next = None

        return new_head

if __name__ == "__main__":
        # Create the linked list: 1 -> 2 -> 3
    list_to_reverse_recursive = ListNode(1, ListNode(2, ListNode(3,)))
    list_to_reverse_iterative = ListNode(1, ListNode(2, ListNode(3, )))

    solution = Solution()

    print("--- Starting Recursive Reversal ---\n")
    reversed_head = solution.reverseListRecursive(list_to_reverse_recursive)
    reversed_head_iterative = solution.reverseListIterative(list_to_reverse_iterative)

    print("\n--- Reversal Complete ---")
    print_list(reversed_head, "Final List")
    print_list(reversed_head_iterative, "Final List")

