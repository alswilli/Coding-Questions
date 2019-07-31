# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        route = []
        route = self.traverse(root, route)
        return route
    
    def traverse(self, root, route):
        if root == None:
            return route
        else:
            route = self.traverse(root.left, route)
            route.append(root.val)
            route = self.traverse(root.right, route)
            return route