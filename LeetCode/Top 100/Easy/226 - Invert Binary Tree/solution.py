# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        root = self.traverse(root)
        return root
        
    def traverse(self, root):
        if root == None:
            return root
        else:
            left = self.traverse(root.left)
            right = self.traverse(root.right)
            root.left = right
            root.right = left
            return root