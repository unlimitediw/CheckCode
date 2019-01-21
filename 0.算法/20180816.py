# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        memo = {}

        def helper(remain,length):
            if remain == 0:
                return [[0,0]]
            cur = (remain,length)
            res = []
            if cur in memo:
                return memo[cur]
            take, nTaken = [],[]
            if remain <= (length+1):
                take = helper(remain - 1, length - 1)
            if remain <= length:
                nTaken = helper(remain, length - 1)
            if length >= 6:
                for ans in take:
                    res.append([2**(length-6) + ans[0],ans[1]])
            else:
                for ans in take:
                    res.append([ans[0],2**length+ans[1]])
            for ans in nTaken:
                res.append(ans)
            memo[cur] = res
            return res
        rawResult = helper(num,9)
        finalRes = []
        for res in rawResult:
            if res[0] < 12 and res[1] < 60:
                finalRes.append(str(res[0])+':'+str(res[1]).zfill(2))
        return finalRes

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        preZero = False
        head = 0
        removeLength = 0
        checkRange = k
        for i in range(0,len(num)):
            if i <= checkRange:
                if preZero:
                    if num[i] != '0':
                        preZero = False
                        head = i
                    else:
                        checkRange += 1
                        head += 1
                else:
                    if num[i] == '0':
                        removeLength = i - head
                        head += removeLength
                        preZero = True
                        checkRange += 1
            else:
                break
        remain = k - removeLength
        finalRes = ''
        res = []
        key = head
        for i in range(head,len(num)):
            if not remain:
                break
            key = i+1
            if not res:
                res = [num[i]]
                continue
            while res:
                if num[i] < res[-1]:
                    res.pop()
                    remain -= 1
                    if remain == 0:
                        key = i
                        break
                    if not res:
                        res.append(num[i])
                        break
                else:
                    res.append(num[i])
                    break
        if remain:
            res = res[:-remain]
        for elem in res:
            finalRes += elem
        finalfinalRes = finalRes + num[key:]
        return finalfinalRes if finalfinalRes else '0'

    def removeKdigitsNew(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) <= k:
            return '0'

        stack = []

        for digit in num:
            while k > 0 and stack and int(stack[-1]) > int(digit):
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0:  # corner case 112 remove 1
            stack.pop()
            k -= 1
        return ''.join(stack).lstrip('0') or '0'

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        if root.left:
            if not root.left.left and not root.left.right:
                res += root.left.val
            else:
                res += self.sumOfLeftLeaves(root.left)
        if root.right:
            res += self.sumOfLeftLeaves(root.right)
        return res

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        def PositiveToHex(num):
            res = ''
            while num != 0:
                cur = num % 16
                num //= 16
                if cur < 10:
                    res += str(cur)
                else:
                    res += chr(cur+87)
            return res[::-1]
        if num == 0:
            return '0'
        elif num > 0:
            return PositiveToHex(num)
        else:
            return PositiveToHex(16**8 + num)

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        heightKeyDic = {}
        newList = []
        tempStack = []
        finalList = []
        innerMemoDic = {}
        for person in people:
            if person[0] not in heightKeyDic:
                heightKeyDic[person[0]] = [person[1]]
            else:
                heightKeyDic[person[0]].append(person[1])
        sortedKeyList = sorted(heightKeyDic.keys())
        for key in sortedKeyList:
            for elem in sorted(heightKeyDic[key])[::-1]:
                newList.append([key,elem])
        for key in heightKeyDic.keys():
            innerMemoDic[key] = 0
        while newList:
            cur = newList.pop()
            if cur[1] != innerMemoDic[cur[0]]:
                tempMemo = innerMemoDic[cur[0]]
                while tempMemo != cur[1]:
                    tempStack.append(finalList.pop())
                    tempMemo -= 1
            finalList.append([cur[0],cur[1]])
            finalList += tempStack[::-1]
            tempStack = []
            for key in sortedKeyList:
                if key <= cur[0]:
                    innerMemoDic[key] += 1
        return finalList

    def reconstructQueueFast(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: x[1])
        people = sorted(people, key=lambda x: -x[0])
        print(people)
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = [0]*52
        res = 0
        haveOdd = 0
        for char in s:
            if ord(char) >= 97:
                memo[ord(char) - 97] += 1
            else:
                memo[ord(char) - 39] += 1
        for val in memo:
            if val % 2 == 0:
                res += val
            else:
                res += val -1 if val > 2 else 0
                haveOdd = 1
        return res + haveOdd

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res

    def numberOfArithmeticSlicesAnother(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #!!!!
        memo =[[957 for col in range(len(A))]for row in range(len(A))]
        iniLength = 3
        endPos = iniLength - 1
        res = 0
        print(A)
        print(memo)
        memo[2][3] = 1
        print(type(memo[2][3]))
        print(memo[4][3],'!!!')
        # !!!!!!!!!!!!! python中 list list如果使用[[?]*len]*len的方法初始化，将导致外部所有相等
        #http://www.cnblogs.com/coderzh/archive/2008/05/18/1201993.html
        while iniLength <= len(A):
            while endPos < len(A):
                if iniLength == 3:
                    if A[endPos] + A[endPos-2] == 2* A[endPos-1]:
                        #print(memo[6][3],endPos,iniLength,'!')
                        memo[endPos][iniLength] = A[endPos] - A[endPos-1]
                        res += 1
                else:
                    if memo[endPos-1][iniLength-1] != 'kstr' and memo[endPos-1][iniLength-1] == A[endPos] - A[endPos-1]:
                        #print(endPos,iniLength,memo[6][3])
                        memo[endPos][iniLength] = A[endPos] - A[endPos-1]
                        res += 1
                endPos += 1
            iniLength += 1
            endPos = iniLength - 1
        print(memo)
        return res


    def numberOfArithmeticSlicesOld(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dic = {}
        iniLength = len(A)
        startPos = 0
        res = 0
        while iniLength >= 3:
            while startPos < len(A) - 2:
                if (startPos,iniLength) in dic or (startPos,iniLength+1) in dic:
                    dic[(startPos,iniLength)] = 1
                    res += 1
                else:
                    isSlice = True
                    for i in range(startPos + 1,startPos + iniLength - 1):
                        if A[i+1] - A[i] != A[i] - A[i-1]:
                            if i - startPos >= 2:
                                print(A[startPos:i+1])
                                dic[(startPos,i-startPos+1)] = 1
                            break
                    if isSlice:
                        dic[(startPos, iniLength)] = 1
                        res += 1
                startPos += 1
            iniLength -= 1
            startPos = 0
        return res

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        Mover = A[1] - A[0]
        lastPos = 1
        for moverPos in range(2,len(A)):
            if A[moverPos] - A[moverPos-1] == Mover:
                res += moverPos - lastPos
            else:
                lastPos = moverPos
                Mover = A[moverPos] - A[moverPos-1]
        return res

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        first = -float('inf')
        second = -float('inf')
        third = -float('inf')
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        return third

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num2) > len(num1):
            temp = num1
            num1 = num2
            num2 = temp
        dist = len(num1) - len(num2)
        num3 = num1[:dist]
        num1 = num1[dist:]
        pos = len(num2) - 1
        carry = 0
        res = ''
        while pos >= 0:
            cur = int(num1[pos]) + int(num2[pos]) + carry
            if cur >= 10:
                cur %= 10
                carry = 1
            else:
                carry = 0
            res += str(cur)
            pos -= 1
        pos = len(num3) - 1
        num3Res = ''

        while pos >= 0:
            if carry == 0:
                num3Res += num3[:pos+1][::-1]
                break
            cur = 1 + int(num3[pos])
            if cur == 10:
                carry = 1
                num3Res += '0'
            else:
                carry = 0
                num3Res += str(cur)
            pos -= 1
        if carry == 1:
            num3Res += '1'
        return num3Res[::-1] + res[::-1]

print(Solution().addStrings('7381','456'))