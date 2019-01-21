class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class PTreeNode(object):
    def __init__(self, x):
        # x is TreeNode
        self.val = x
        self.parent = None


class Solution(object):

    # L236
    def lowestCommonAncestorOld(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        self.res = None
        self.pVal = p.val
        self.qVal = q.val
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if self.res or not root:
            return False, False
        pExist = False
        qExist = False
        if root.val == self.pVal:
            pExist = True
        elif root.val == self.qVal:
            qExist = True
        pExist = pExist | self.dfs(root.left)[0] | self.dfs(root.right)[0]
        qExist = qExist | self.dfs(root.left)[1] | self.dfs(root.right)[1]
        if pExist and qExist:
            self.res = root
        return pExist, qExist

    # Bfs method
    def lowestCommonAncestorOld2(self, root, p, q):
        if not root:
            return None
        levelList = [[root]]
        cur = [root]
        next = []
        while True:
            curRoot = cur.pop()
            if curRoot.left:
                next.append(curRoot.left)
            if curRoot.right:
                next.append(curRoot.right)
            if not cur:
                levelList.append(next[:])
                cur = next
                next = []

        # Bfs not work!

    # ParentTreeMode
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        self.pFinal = None
        self.qFinal = None
        self.p2Val = p.val
        self.q2Val = q.val
        pNode = PTreeNode(root)
        self.dfs2(root, pNode)
        pList = [self.pFinal]
        qList = [self.qFinal]
        while self.pFinal.parent:
            self.pFinal = self.pFinal.parent
            pList.insert(0, self.pFinal)
        while self.qFinal.parent:
            self.qFinal = self.qFinal.parent
            qList.insert(0, self.qFinal)
        for i in range(min(len(pList), len(qList))):
            if pList[i].val.val != qList[i].val.val:
                return pList[i - 1].val
        if len(pList) < len(qList):
            return pList[-1].val
        else:
            return qList[-1].val

    def dfs2(self, root, parentNode):
        if root.val == self.p2Val:
            self.pFinal = parentNode
        if root.val == self.q2Val:
            self.qFinal = parentNode
        if root.left:
            newPNode = PTreeNode(root.left)
            newPNode.parent = parentNode
            self.dfs2(root.left, newPNode)
        if root.right:
            newPNode = PTreeNode(root.right)
            newPNode.parent = parentNode
            self.dfs2(root.right, newPNode)

    # 第一次的更改
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(root, val):
            if not root:
                return False
            if root == val:
                return True
            return dfs(root.left, val) or dfs(root.right, val)

        if dfs(p, q):
            return p
        if dfs(q, p):
            return q
        while True:
            if dfs(root.left, p) and dfs(root.left, q):
                root = root.left
            elif dfs(root.right, p) and dfs(root.right, q):
                root = root.right
            else:
                return root

    # 总结 dfs时考虑方向性和目的性

    # L237
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        tmp = node
        while tmp.next:
            tmp.val = tmp.next.val
            if tmp.next.next:
                tmp = tmp.next
            else:
                tmp.next = None

    # L238
    # Without division and O(n)
    # ~left triangle and right triangle
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        mul = 1
        for i in range(0, n):
            res.append(mul)
            mul *= nums[i]
        mul = 1
        for i in range(n - 1, -1, -1):
            res[i] *= mul
            mul *= nums[i]
        return res

    def searchMatrixOld(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        keyPoint = 0
        n = min(len(matrix[0]), len(matrix))
        remainMatrix = []
        for i in range(0, n):
            if target < matrix[i][i]:
                keyPoint = i
                break
            elif target == matrix[i][i]:
                return True
        if len(matrix) > n:
            remainMatrix = matrix[n:]
        elif len(matrix[0]) > n:
            remainMatrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))][n:]
        ldRemainMatrix = [[matrix[i][j] for j in range(0, keyPoint)] for i in range(keyPoint, len(matrix))]
        ruRemainMatrix = [[matrix[i][j] for j in range(keyPoint, len(matrix[0]))] for i in range(0, keyPoint)]
        return self.searchMatrix(remainMatrix, target) or self.searchMatrix(ldRemainMatrix,
                                                                            target) or self.searchMatrix(ruRemainMatrix,
                                                                                                         target)

    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        return self.spSearchMatrix(matrix, target, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)

    def spSearchMatrix(self, matrix, target, va, vb, ha, hb):
        if va > len(matrix)-1 or vb > len(matrix)-1 or va < 0 or vb < 0 or ha > len(matrix[0])-1 or hb > len(matrix[0])-1 or ha < 0 or hb < 0 or va > vb or ha > hb:
            return False
        print(va,vb,ha,hb)
        if va == vb and ha == hb:
            if matrix[va][ha] == target:
                return True
            return False
        n = min(vb - va, hb - ha) + 1
        keyPoint = 0
        if target < matrix[va][ha]:
            return False
        for i in range(0, n):
            if target < matrix[va + i][ha + i]:
                keyPoint = i
                break
            elif target == matrix[va + i][ha + i]:
                return True
        print(keyPoint)
        ans = False
        if vb - va + 1 > n:
            ans |= self.spSearchMatrix(matrix, target, va + n, vb, ha, hb)
        elif hb - ha + 1 > n:
            ans |= self.spSearchMatrix(matrix, target, va, vb, ha + n, hb)
        return ans or self.spSearchMatrix(matrix,target,keyPoint+va,vb,ha,keyPoint+ha-1) or self.spSearchMatrix(matrix, target,
            va, keyPoint+va-1, keyPoint+ha, hb)

    def searchMatrixImprove(self,matrix,target):

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        while len(matrix) > 0:
            if matrix[-1][-1] < target:
                return False
            else:
                if matrix[-1][0] > target:
                    del matrix[-1]
                else:
                    if target in matrix[-1]:
                        return True
                    else:
                        del matrix[-1]
        return False

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        newInput = []
        i = 0
        while i < len(input):
            if ord(input[i]) < 48 or ord(input[i]) > 57:
                newInput.append(input[i])
            else:
                cur = int(input[i])
                i += 1
                while i < len(input):
                    if 47<ord(input[i]) <58:
                        cur = cur*10 + int(input[i])
                        i += 1
                    else:
                        break
                i -= 1
                newInput.append(cur)
            i+= 1
        res = self.iter(newInput)
        return res

    def iter(self,input):
        if len(input) == 1:
            return [int(input[0])]
        else:
            res = []
            for i in range(1,len(input),2):
                p1 = self.iter(input[:i])
                p2 = self.iter(input[i+1:])
                for x in range(len(p1)):
                    for y in range(len(p2)):
                        res.append(self.operate(p1[x],p2[y],input[i]))
            return res


    def operate(self,a,b,char):
        if char == '+':
            return a + b
        elif char == '-':
            return a - b
        elif char == '*':
            return a * b

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        for char in t:
            if char not in dic:
                return False
            else:
                dic[char] -= 1
                if dic[char] == 0:
                    del dic[char]
        if dic:
            return False
        return True

    # set!
    def isAngramSet(self,s,t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (set(s) != set(t)) or (len(s) != len(t)):
            return False

        for i in set(s):
            if s.count(i) != t.count(i):
                return False

        return True

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return
        self.res = []
        self.inheriter(root,str(root.val))
        return self.res

    def inheriter(self,root,path):
        if not root.left and not root.right:
            self.res.append(path)
            return
        if root.left:
            newPath = path + '->' + str(root.left.val)
            self.inheriter(root.left,newPath)
        if root.right:
            newPath = path + '->' + str(root.right.val)
            self.inheriter(root.right,newPath)

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        newNum = 0
        while num >= 1:
            newNum += num % 10
            num = num // 10
        return self.addDigits(newNum)

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 0:
            return False
        while num != 1:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            else:
                return False
        return True



    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ugly = sorted([2 ** a * 3 ** b * 5 ** c for a in range(32) for b in range(20) for c in range(14)])
        return self.ugly[n - 1] if n > 0 else None

    def nthUglyNumberBetter(self,n):
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]


print(int(3**0.5))
