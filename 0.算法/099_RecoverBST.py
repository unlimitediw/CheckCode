# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        我的解 其实里面在优化下连续llrr的情况就可以完成，心情不好不继续做了，过了1000例，卡在连续上了
        second = root; // 如果两个调换的元素相邻，则应采用该设置 和标准答案就差这个了，自己写的太复杂了，下次麻烦的题先认真写好伪代码
        """
        min_TreeNode = TreeNode(float("-inf"))
        max_TreeNode = TreeNode(float("inf"))
        double_error = []
        single_error = []
        first_mode = 0
        if not root:
            return
        else:
            if root.left:
                if root.left.val >= root.val:
                    first_mode+=1
                    double_error.append(root.left)
                    single_error.append(root)
                    single_error.append(root.left)
                    if root.left.left:
                        if root.left.left.val >= root.left.val:
                            double_error[0] = root
                            double_error.append(root.left.left)
                            self.swap(double_error[0],double_error[1])
                        self.recurssion_BST(root.left.left, min_TreeNode, root, double_error, single_error)
                    if root.left.right:
                        if root.left.right.val <= root.val:
                            double_error[0] = root
                            double_error.append(root.left.right)
                            self.swap(double_error[0],double_error[1])
                        self.recurssion_BST(root.left.right, min_TreeNode, root, double_error, single_error)
                else:
                    self.recurssion_BST(root.left, min_TreeNode, root, double_error, single_error)

            if root.right:
                if root.right.val <= root.val:
                    first_mode+=1
                    double_error.append(root.right)
                    single_error.append(root)
                    single_error.append(root.right)
                    if root.right.left:
                        if root.right.left.val >= root.val:
                            double_error[0] = root
                            double_error.append(root.right.left)
                            self.swap(double_error[0],double_error[1])
                        self.recurssion_BST(root.right.left, root, max_TreeNode, double_error, single_error)
                    if root.right.right:
                        if root.right.right.val <=root.right.val:
                            double_error[0] = root
                            double_error.append(root.right.right)
                            self.swap(double_error[0],double_error[1])
                        print(root.val,root.right.right.val)
                        self.recurssion_BST(root.right.right, root, max_TreeNode, double_error, single_error)
                else:
                    self.recurssion_BST(root.right, root, max_TreeNode, double_error, single_error)
            if len(double_error) == 1:
                self.swap(single_error[0], single_error[1])
            if first_mode == 2:
                self.swap(double_error[0],double_error[1])
        return

    def recurssion_BST(self, root, parent_min, parent_max, double_error, single_error):
        print(root.left,root.right)
        if root.left:
            if parent_max.val > root.val:
                new_parent_max = root
            else:
                new_parent_max = parent_max
            if parent_min.val < root.left.val < new_parent_max.val:
                self.recurssion_BST(root.left, parent_min, new_parent_max, double_error, single_error)
            else:
                double_error.append(root.left)
                if parent_min.val >= root.left.val:
                    single_error.append(root.left)
                    single_error.append(parent_min)
                elif root.left.val >= new_parent_max.val:
                    single_error.append(root.left)
                    single_error.append(new_parent_max)
                if len(double_error) == 2:
                    self.swap(double_error[0], double_error[1])
                    return
                self.recurssion_BST(root.left, parent_min, parent_max, double_error, single_error)
        if root.right:
            if parent_min.val < root.val:
                new_parent_min = root
            else:
                new_parent_min = parent_min
            if new_parent_min.val < root.right.val < parent_max.val:
                self.recurssion_BST(root.right, new_parent_min, parent_max, double_error, single_error)
            else:
                double_error.append(root.right)
                if new_parent_min.val >= root.right.val:
                    single_error.append(root.right)
                    single_error.append(new_parent_min)
                elif root.right.val >= parent_max.val:
                    single_error.append(root.right)
                    single_error.append(parent_max)
                if len(double_error) == 2:
                    self.swap(double_error[0], double_error[1])
                    return
                self.recurssion_BST(root.right, parent_min, parent_max, double_error, single_error)

    def swap(self, A, B):
        tmp = A.val
        A.val = B.val
        B.val = tmp

a = Solution()
root = TreeNode(3)
root.right = TreeNode(1)
root.right.left = TreeNode(2)


a.recoverTree(root)
print(root.val,root.right.val)


