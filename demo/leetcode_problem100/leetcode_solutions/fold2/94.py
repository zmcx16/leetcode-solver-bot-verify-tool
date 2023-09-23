class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node):
            if node is None:
                return []
            left = helper(node.left)
            right = helper(node.right)
            return left + [node.val] + right
        return helper(root)