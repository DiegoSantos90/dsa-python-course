'''
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Time Complexity: O(n)  # Single pass through all nodes
Space Complexity: O(h)  # Space for recursion stack, where h is the height of the tree
'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = None

        if node is not None:
            print(f"{'  ' * level}{prefix}{node.val}")
            if node.left:
                self.print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.print_tree(node.right, level + 1, "R--- ")

if __name__ == "__main__":

    solution = Solution()

    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    solution.print_tree(root)

    solution.invertTree(root)
    solution.print_tree(root)
