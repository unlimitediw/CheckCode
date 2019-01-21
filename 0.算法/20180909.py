# 900
# 看清 start from today
import bisect
class StockSpannerFreeDay(object):

    def __init__(self):
        self.pre = float('inf')
        self.ans = []
        self.dic = {}
        self.sortAns = []
        self.prelength = 1

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if price > self.pre:
            self.prelength += 1
            self.ans.append(max(self.prelength, self.findSmallerOne(price)))
        else:
            self.prelength = 1
            self.ans.append(self.findSmallerOne(price))

        self.pre = price

    def findSmallerOne(self, val):
        pos = bisect.bisect_left(self.sortAns,val)
        max = self.dic[pos]
        return None

class StockSpanner(object):

    def __init__(self):
        self.memo = []
        self.ans =[]
        self.curPos = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        conLength = 1
        curPos = self.curPos - 1
        while curPos >= 0 and self.memo[curPos] <= price:
            conLength += self.ans[curPos]
            curPos -= self.ans[curPos]
        self.memo.append(price)
        self.ans.append(conLength)
        self.curPos += 1
        return conLength



a = [1,2,3,7,9]
print(bisect.bisect_left(a,6))

