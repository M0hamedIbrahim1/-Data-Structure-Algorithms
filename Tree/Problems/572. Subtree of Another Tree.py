# link   : https://leetcode.com/problems/subtree-of-another-tree/description/
# author : Mohamed Ibrahim

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # Check for all subtree rooted at all nodes of tree "root"
        def dfs(node):
            if not node:return
            elif is_identical(node, subRoot):return True
            return dfs(node.left) or dfs(node.right)

        def is_identical(node1, node2):

            if node1 is None or node2 is None:
                return  node1 is None and node2 is None
            if node1.val != node2.val:
                return False
            return is_identical(node1.left, node2.left) and is_identical(node1.right, node2.right)


        return dfs(root)
        
