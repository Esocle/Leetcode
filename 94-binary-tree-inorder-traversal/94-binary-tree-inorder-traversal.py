# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if root == None: return []
        temp = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            temp.append(root.val)
            if root.right:
                inorder(root.right)
                
        inorder(root)
        return temp