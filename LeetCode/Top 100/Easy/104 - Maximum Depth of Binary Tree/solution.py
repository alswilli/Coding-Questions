# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        maxDepth = 0
        currDepth = 0
        maxDepth = self.traverse(root, currDepth, maxDepth)
        return maxDepth
    
    def traverse(self, root, currDepth, maxDepth):
        if root == None:
            return currDepth
        else:
            currDepth += 1
            if currDepth > maxDepth:
                maxDepth = currDepth
            print("ROOT")
            print("currDepth: " + str(currDepth))
            print("maxDepth: " + str(maxDepth))
            print("val: " + str(root.val))
            print()
            leftDepth = self.traverse(root.left, currDepth, maxDepth)
            if leftDepth > maxDepth:
                maxDepth = leftDepth
            print("LEFT")
            print("currDepth: " + str(currDepth))
            print("maxDepth: " + str(maxDepth))
            print("val: " + str(root.val))
            print()
            rightDepth = self.traverse(root.right, currDepth, maxDepth)
            if rightDepth > maxDepth:
                maxDepth = rightDepth
            print("RIGHT")
            print("currDepth: " + str(currDepth))
            print("maxDepth: " + str(maxDepth))
            print("val: " + str(root.val))
            print()
            # if leftDepth > maxDepth:
            #     maxDepth = leftDepth
            # elif rightDepth > maxDepth:
            #     maxDepth = rightDepth
            return maxDepth
                