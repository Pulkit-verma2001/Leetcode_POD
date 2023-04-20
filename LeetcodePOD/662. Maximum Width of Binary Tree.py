# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #***********************************************************************
    #  
    #***********************************************************************

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        queue=[(root,0)]
        ans=0
        while len(queue):
            n=len(queue)
            for i in range(n):
                node,idx=queue.pop(0)
                if i==0 : first=idx
                if i==n-1 : last=idx
                if node.left:
                    queue.append((node.left,idx*2+1))
                if node.right:
                    queue.append((node.right,idx*2+2))
            ans=max(ans,last-first+1)
        return ans
        


    #***********************************************************************
    #  TLE
    #***********************************************************************

    # def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     queue=[root]
    #     result=[]
    #     while len(queue):
    #         lst=[]
    #         l=[]
    #         while len(queue):
    #             node=queue.pop(0)
    #             if node!=-1:
    #                 l.append(node.val)
    #             if node==-1:
    #                 l.append(-1)
    #                 lst.append(-1)
    #                 lst.append(-1)
    #                 # continue
    #             else:
    #                 if node.left==None:
    #                     lst.append(-1)
    #                 if node.left:
    #                     lst.append(node.left)
    #                 if node.right:
    #                     lst.append(node.right)
    #                 if node.right==None:
    #                     lst.append(-1)
        
    #         queue=lst
    #         result.append(l)
    #         l1=list(set(lst))
    #         if len(l1)==1 and l1[0]==-1:
    #             break
    #     ans=0
    #     for lst in result:
    #         i=0
    #         while i<len(lst) and lst[i]==-1:
    #             i+=1
    #         j=len(lst)-1
    #         while j>=0 and lst[j]==-1:
    #             j-=1
    #         ans=max(ans,j-i+1)
    #     return ans