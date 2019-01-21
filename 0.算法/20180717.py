class Solution:

    # p189
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        t = nums[-k:] + nums[:-k]
        for i in range(len(t)):
            nums[i] = t[i]

    def rotate1(self, nums, k):
        k = k % len(nums)
        for i in range(k):
            a = nums.pop(-1)
            nums.insert(0, a)

    # p190
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(31, -1, -1):
            if n >= 2 ** i:
                res += 2 ** (31 - i)
                n -= 2 ** i
        return res

    # p191
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(31, -1, -1):
            if n >= 2 ** i:
                n -= 2 ** i
                count += 1
        return count

    # p199
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.curLevel = 0
        self.res = [root.val]
        self.traversal(root, 0)
        return self.res

    def traversal(self, root, level):
        if level > self.curLevel:
            self.res.append(root.val)
            self.curLevel = level
        if root.right:
            self.traversal(root.right, level + 1)
        if root.left:
            self.traversal(root.left, level + 1)

    # p200
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        self.islandDic = {}
        self.grid = grid
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1' and (x, y) not in self.islandDic:
                    count += 1
                    self.checkIsland((x, y))
        return count

    def checkIsland(self, position):
        if position[0] < 0 or position[0] == len(self.grid) or position[1] < 0 or position[1] == len(self.grid[0]) or \
                self.grid[position[0]][position[1]] == '0' or (position[0], position[1]) in self.islandDic:
            return
        self.islandDic[(position[0], position[1])] = 0
        self.checkIsland([position[0] + 1, position[1]])
        self.checkIsland([position[0] - 1, position[1]])
        self.checkIsland([position[0], position[1] + 1])
        self.checkIsland([position[0], position[1] - 1])

    # p201
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while n > m:
            n &= n-1
        return n

    # p202
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.n = n
        self.dic = {}
        return self.isHappyIter(n)

    def isHappyIter(self,n):
        if n in self.dic:
            return False
        else:
            self.dic[n] = 1
        res = 0
        for i in str(n):
            res += int(i)**2
        if res == 1:
            return True
        else:
            return self.isHappyIter(res)

    # p203
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        while head.val == val:
            if head.next:
                head = head.next
            else:
                return None
        start = head
        pre = head
        while head.next:
            head = head.next
            if head.val == val:
                pre.next = head.next
            else:
                pre = head
        return start

    # p204 **
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        s = [1] * n
        s[0] = 0
        s[1] = 0
        for i in range(2,int(n**0.5)+1):
            if s[i] == 1:
                s[i*i:n:i] = [0]*int((n-1-i*i)/i+1)
        return sum(s)

    # p 205
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = []
        t_list = []
        s_dic = {}
        t_dic = {}
        for i in range(len(s)):
            if s[i] not in s_dic:
                s_dic[s[i]] = i
                s_list.append(i)
            else:
                s_list.append(s_dic[s[i]])
            if t[i] not in t_dic:
                t_dic[t[i]] = i
                t_list.append(i)
            else:
                t_list.append(t_dic[t[i]])
        if s_list == t_list:
            return True
        else:
            return False

a = [1,2,3]
b = [1,2,4]
print(a == b)



