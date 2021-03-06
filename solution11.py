"""
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \    
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges 
between them.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def height(node): 
    
    if node is None: 
        return 0; 

    return 1 + max(height(node.left), height(node.right)) 


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
    
        if root is None: 
            return 0 

        left_height = height(root.left) 
        right_height = height(root.right)

        left_diameter = self.diameterOfBinaryTree(root.left) 
        right_diameter = self.diameterOfBinaryTree(root.right) 
        max_diameter = max(left_diameter, rightdiameter)

        return(max(left_height + right_height, max_diameter))