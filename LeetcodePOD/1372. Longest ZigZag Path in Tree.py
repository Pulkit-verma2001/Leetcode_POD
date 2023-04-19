class Solution:
    def longestZigZag(self, root: TreeNode) -> int:	
        self.ans = 0
        def solve(root):
            if not root: return (-1,-1) 				
            l1,r1 = solve(root.left)
            l2,r2 = solve(root.right)
			
            self.ans = max(self.ans, max(r1 + 1, l2 + 1))
            return (r1 + 1, l2 + 1)
			
        solve(root)
        return self.ans