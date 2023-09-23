class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateTreesHelper(start, end):
            if start > end:
                return [None]
            result = []
            for i in range(start, end + 1):
                left_subtrees = generateTreesHelper(start, i - 1)
                right_subtrees = generateTreesHelper(i + 1, end)
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        result.append(root)
            return result
        return generateTreesHelper(1, n) if n > 0 else []