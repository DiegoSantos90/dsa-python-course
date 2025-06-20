'''
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down
to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2


Constraints:
The number of nodes in the tree is in the range [0, 104].
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
    def maxDepthRecursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepthRecursive(root.left)
        right_depth = self.maxDepthRecursive(root.right)
        
        return max(left_depth, right_depth) + 1
    
    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return max_depth

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
    print(f"expected: 3, actual: {solution.maxDepthRecursive(root)} \n")  # Output: 3

    root = TreeNode(1, None, TreeNode(2))
    solution.print_tree(root)
    print(f"expected: 2, actual: {solution.maxDepthRecursive(root)} \n")  # Output: 2

    root = None
    solution.print_tree(root)
    print(f"expected: 0, actual: {solution.maxDepthRecursive(root)} \n")  # Output: 2  # Output: 0

    root = TreeNode(1)
    solution.print_tree(root)
    print(f"expected: 1, actual: {solution.maxDepthRecursive(root)} \n")  # Output: 2  # Output: 1

    root = TreeNode(1, TreeNode(2))
    print(f"expected: 2, actual: {solution.maxDepthRecursive(root)}")  # Output: 2




