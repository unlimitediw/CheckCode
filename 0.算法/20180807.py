class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        k = len(primes)
        idxList = [0]*k
        uglyNumList = [1] *k
        while n > 1:
            for uglyIdx in range(k):
                uglyNumList[ugly] = primes[uglyIdx] * ugly[idxList[uglyIdx]]
            uglyMin = min(uglyNumList)
            for numIdx in range(k):
                if uglyMin == uglyNumList[numIdx]:
                    idxList[numIdx] += 1
            ugly.append(uglyMin)
            n -= 1
        return ugly[-1]

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # database
        setMemo = []
        for word in words:
            setMemo.append(set(word))
        maxLen = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if self.compareWord(setMemo[i],setMemo[j]) and len(words[i])*len(words[j]) > maxLen:
                    maxLen = len(words[i])*len(words[j])
        return maxLen

    def compareWord(self,setA,setB):
        for char in setA:
            if char in setB:
                return False
        return True

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int(math.sqrt(n))
        bulbList = [1] * n
        i = 2
        while i <= n:
            for k in range(1,n//i+1):
                bulbList[i*k-1] *= -1
        res = 0
        for state in bulbList:
            if state == 1:
                res += 1
        return res

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coinsQueue = []
        nextQueue = []
        curLength = 1
        c = 0
        for coin in coins:
            if coin == amount:
                return 1
            coinsQueue.append(coin)
        while coinsQueue:
            curCoin = coinsQueue.pop()
            for coin in coins:
                c+=1
                val = curCoin + coin
                if val == amount:
                    return curLength+1
                elif val < amount and val not in nextQueue:
                    nextQueue.append(curCoin+coin)
            if not coinsQueue:
                print(nextQueue)
                coinsQueue = nextQueue
                nextQueue = []
                curLength += 1
        return -1

    def coinChangeDeep(self,coins,amount):
        for i in range(len(coins)):
            if amount == coins[i]:
                return

    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Astar
        import math
        changeDic = {}
        changeDic[0] = [[amount,0]]
        while changeDic:
            curKey = min(changeDic.keys())
            curVal = changeDic[curKey].pop()
            print(curVal)
            if not changeDic[curKey]:
                del changeDic[curKey]
            for coin in coins:
                remain = curVal[0] - coin
                if remain == 0:
                    return curVal[1] + 1
                elif remain < 0:
                    continue
                curMax = 1
                for coin in coins:
                    if coin < remain:
                        curMax = coin
                    else:
                        break
                if curVal[1] + 1 + math.ceil(remain/curMax) not in changeDic:
                    changeDic[curVal[1] + 1 + math.ceil(remain/curMax)] = [[remain,curVal[1] + 1]]
                else:
                    changeDic[curVal[1] + 1 + math.ceil(remain / curMax)].append([remain, curVal[1] + 1])
        return -1

    def coinChange3(self,coins,amount):
        self.amountDic = {}
        self.coins = coins
        if amount == 0:
            return 0
        res = self.coinChangeDeep3(amount)
        print(res)
        if res > 99998:
            return -1
        else:
            return res

    def coinChangeDeep3(self,amount):
        if amount in self.amountDic:
            return self.amountDic[amount]
        minStep = 99999
        for coin in self.coins:
            if coin == amount:
                return 1
            elif coin > amount:
                continue
            elif self.coinChangeDeep3(amount - coin) < minStep:
                minStep = self.coinChangeDeep3(amount - coin)
        self.amountDic[amount] = minStep+1
        return minStep + 1

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nums = sorted(nums)
        newNum = []
        i = 0
        j = len(nums) - 1
        while i <= j:
            if i == j:
                newNum.append(nums[i])
            else:
                newNum.append(nums[i])
                newNum.append(nums[j])
                i += 1
                j -= 1
        for i in range(len(nums)):
            nums[i] = newNum[i]


nums = [3,2,1,7]
nums = sorted(nums)
print(nums)
print(Solution().coinChange3([1,2147483647],2))