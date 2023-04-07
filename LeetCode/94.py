class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lis = []
        curr = root
        whle(curr):
            if curr.left == None:
                lis.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right == None:
                    prev.right = curr
                    curr = curr.left
                else:
                    lis.append(curr.val)
                    curr = curr.right
                    prev.right = None
            else lis
