#Leetcode: 104
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def maxDepth(root: TreeNode) -> int:
    if(root==None):
        return 0
    return max(maxDepth(root.left), maxDepth(root.right))+1