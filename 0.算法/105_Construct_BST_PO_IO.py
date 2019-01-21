# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if any(preorder):
            root = TreeNode(preorder[0])
            for i in range(len(inorder)):
                if inorder[i] == root.val:
                    left_preorder = []
                    left_inorder = inorder[:i]
                    for j in preorder:
                        if j in left_inorder:
                            left_preorder.append(j)
                    right_preorder = []
                    right_inorder = inorder[i + 1:]
                    for j in preorder:
                        if j in right_inorder:
                            right_preorder.append(j)
                    print(right_preorder,right_inorder)
                    print(left_preorder,left_inorder)
                    if any(left_inorder):
                        repre_left = root
                        for i in range(len(left_preorder)):
                            if left_preorder[i] == left_inorder[-1-i]:
                                repre_left.left = TreeNode(left_preorder[i])
                                repre_left = repre_left.left
                            else:
                                repre_left.left = self.buildTree(left_preorder[i:], left_inorder[:len(left_inorder)-i])
                                break
                    if any(right_inorder):
                        repre_right = root
                        for i in range(len(right_preorder)):
                            if right_preorder[i] == right_inorder[i]:
                                repre_right.right = TreeNode(right_preorder[i])
                                repre_right = repre_right.right
                            else:
                                repre_right.right = self.buildTree(right_preorder[i:], right_inorder[i:])
                                break
                    break

            return root
        else:
            return

a = Solution()
print(a.buildTree([4,3,1,2],[1,2,3,4]).left.left.val)
a = [1,2,3,4]
print(a[:4])