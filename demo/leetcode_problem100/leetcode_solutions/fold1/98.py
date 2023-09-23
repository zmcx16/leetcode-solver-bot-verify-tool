class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, lower_bound, upper_bound):
            if not node:
                return True
            if node.val <= lower_bound or node.val >= upper_bound:
                return False
            return is_valid(node.left, lower_bound, node.val) and is_valid(node.right, node.val, upper_bound)
        return is_valid(root, float('-inf'), float('inf'))