class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j + 1])


# database way
class NumMatrixNew(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.dic = {}
        dic2 = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                box = []
                z = j + 1
                while z <= len(matrix[0]):
                    box.append(sum(matrix[i][j:z]))
                    z += 1
                dic2[(i, j)] = box

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                box = [[0 for a in range(len(matrix[0]) - j)] for b in range(len(matrix) - i)]
                x = 0
                while x < len(matrix) - i:
                    y = 0
                    while y < len(matrix[0]) - j:
                        for r in range(i, i + x + 1):
                            box[x][y] += dic2[(r, j)][y]
                        y += 1
                    x += 1
                self.dic[(i, j)] = box

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dic[(row1, col1)][row2 - row1][col2 - col1]


# dp way
class NumMatrix3(object):

    # 大正方减小正方去掉两个余正方进行DP
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.sum = None
            return
        h, w = len(matrix), len(matrix[0])
        self.sum = [[0] * w for i in range(h)]
        for i in range(h):
            tmp = 0
            for j in range(w):
                tmp2 = 0 if i == 0 else self.sum[i - 1][j]
                self.sum[i][j] = tmp + matrix[i][j] + tmp2
                tmp += matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # assert self.sum
        blk1 = 0 if row1 == 0 else self.sum[row1 - 1][col2]
        blk2 = 0 if col1 == 0 else self.sum[row2][col1 - 1]
        blk3 = 0 if row1 == 0 or col1 == 0 else self.sum[row1 - 1][col1 - 1]
        blk4 = self.sum[row2][col2]
        return blk4 - blk1 - blk2 + blk3


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        sPtr = 2
        self.res = False
        while not self.res and sPtr < len(num):
            fPtr = 1
            while fPtr < sPtr:
                if (fPtr > 1 and num[0] == '0') or (sPtr - fPtr > 1 and num[fPtr] == '0'):
                    pass
                else:
                    newSeq = [int(num[:fPtr]), int(num[fPtr:sPtr])]
                    newRem = num[sPtr:]
                    self.judgeConstruct(newSeq, newRem)
                fPtr += 1
            sPtr += 1
        return self.res

    def judgeConstruct(self, numSeq, remain):
        if len(remain) > 1 and remain[0] == '0':
            return
        if self.res:
            return
        for length in range(1, len(remain) + 1):
            dic = {}
            curNum = int(remain[:length])
            correct = False
            if curNum == numSeq[-1] + numSeq[-2]:
                correct = True
            '''
                同时判断前面所有数
                for num in numSeq:
                    if curNum < num:
                        continue
                    else:
                        if num not in dic:
                            dic[curNum - num] = 0
                        else:
                            correct = True
            '''

            if correct:
                if length == len(remain):
                    self.res = True
                newSeq = numSeq[:]
                newSeq.append(curNum)
                self.judgeConstruct(newSeq, remain[length:])

    # sell buy with cooldown
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.prices = prices
        self.profitDic = {}
        return self.dp(0)

    def dp(self, pos):
        maxProfit = 0
        while pos < len(self.prices) - 1 and self.prices[pos] > self.prices[pos + 1]:
            pos += 1
        for i in range(pos, len(self.prices)):
            if i + 2 not in self.profitDic:
                self.profitDic[i + 2] = self.dp(i + 2)
            if i + 1 not in self.profitDic:
                self.profitDic[i + 1] = self.dp(i + 1)
            profit = max(self.prices[i] - self.prices[pos] + self.profitDic[i + 2], self.profitDic[i + 1])
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit

    def maxProfitDp2(self, prices):
        profitDic = {}
        profitDic[len(prices)] = 0
        profitDic[len(prices) + 1] = 0
        profitDic[len(prices) - 1] = 0
        for pos in range(len(prices) - 2, -1, -1):
            maxProfit = 0
            for i in range(pos, len(prices)):
                profit = max(prices[i] - prices[pos] + profitDic[i + 2], profitDic[i + 1])
                if profit > maxProfit:
                    maxProfit = profit
            profitDic[pos] = maxProfit
        return profitDic[0]

    def maxProfitState(self, prices):
        # dp1, dp2, dp3 = 0 stock(cool), 0 stock(no-cool), 1 stock(no-cool)
        dp1, dp2, dp3 = 0, 0, -float("inf")
        for p in prices:
            dp1, dp2, dp3 = dp3 + p, max(dp1, dp2), max(dp2 - p, dp3)
        return max(dp1, dp2)

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        nodeDic = {}
        nodeQueue = []
        nextQueue = []
        findAns = False
        Ans = []
        countDic = {}
        for node in range(n):
            countDic[node] = 1
            nodeDic[node] = []
        for edge in edges:
            nodeDic[edge[0]].append(edge[1])
            nodeDic[edge[1]].append(edge[0])
        # format [root,history,cur]
        for node in range(n):
            nodeQueue.append([node, -1, node])
        while nodeQueue:
            cur = nodeQueue.pop()
            for nextNode in nodeDic[cur[2]]:
                if nextNode != cur[1]:
                    nextQueue.append([cur[0], cur[2], nextNode])
                    countDic[cur[0]] += 1
            countDic[cur[0]] -= 1
            if countDic[cur[0]] == 0:
                findAns = True
                Ans.append(cur[0])
            if not nodeQueue:
                if findAns:
                    print(Ans)
                    return Ans
                nodeQueue = nextQueue
                nextQueue = []
        return []

    # Wrong, should check all graph point
    def findMinHeightTrees2(self, n, edges):
        nodeDic = {}
        memoDic = {}
        nodeQueue = []
        nextQueue = []
        removeList = []
        findAns = False
        count = 0
        if n == 1:
            return [0]
        for node in range(n):
            nodeDic[node] = []
            memoDic[node] = []
        for edge in edges:
            nodeDic[edge[0]].append(edge[1])
            nodeDic[edge[1]].append(edge[0])
            memoDic[edge[0]].append(edge[1])
            memoDic[edge[1]].append(edge[0])
            count += 2
        for key, val in nodeDic.items():
            # format [val,hitory,from]
            if len(val) == 1:
                nodeQueue.append([key, -1])
        while nodeQueue:
            cur = nodeQueue.pop()
            countNodeDic = {}
            for nextNode in nodeDic[cur[0]]:
                if nextNode != cur[1]:
                    if cur[0] in nodeDic[nextNode]:
                        removeList.append((nextNode, cur[0]))
                        if cur[0] not in countNodeDic:
                            countNodeDic[cur[0]] = 0
                        else:
                            countNodeDic[cur[0]] += 1
                    nextQueue.append([nextNode, cur[0]])
            if not nodeQueue:
                for remover in removeList:
                    if remover[1] in nodeDic[remover[0]]:
                        nodeDic[remover[0]].remove(remover[1])
                        count -= 1
                        if count == 0:
                            findAns = True
                if findAns:
                    Ans = []
                    center = False
                    for key, val in countNodeDic.items():
                        if val > 0:
                            center = True
                        Ans.append(key)
                    if center:
                        return Ans

                    else:
                        for key in countNodeDic.keys():
                            for val in memoDic[key]:
                                if val in countNodeDic:
                                    Ans.append(val)

                        return Ans
                nodeQueue = nextQueue
                nextQueue = []
                removeList = []


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j + 1])


# database way
class NumMatrixNew(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.dic = {}
        dic2 = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                box = []
                z = j + 1
                while z <= len(matrix[0]):
                    box.append(sum(matrix[i][j:z]))
                    z += 1
                dic2[(i, j)] = box

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                box = [[0 for a in range(len(matrix[0]) - j)] for b in range(len(matrix) - i)]
                x = 0
                while x < len(matrix) - i:
                    y = 0
                    while y < len(matrix[0]) - j:
                        for r in range(i, i + x + 1):
                            box[x][y] += dic2[(r, j)][y]
                        y += 1
                    x += 1
                self.dic[(i, j)] = box

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dic[(row1, col1)][row2 - row1][col2 - col1]


# dp way
class NumMatrix3(object):

    # 大正方减小正方去掉两个余正方进行DP
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.sum = None
            return
        h, w = len(matrix), len(matrix[0])
        self.sum = [[0] * w for i in range(h)]
        for i in range(h):
            tmp = 0
            for j in range(w):
                tmp2 = 0 if i == 0 else self.sum[i - 1][j]
                self.sum[i][j] = tmp + matrix[i][j] + tmp2
                tmp += matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # assert self.sum
        blk1 = 0 if row1 == 0 else self.sum[row1 - 1][col2]
        blk2 = 0 if col1 == 0 else self.sum[row2][col1 - 1]
        blk3 = 0 if row1 == 0 or col1 == 0 else self.sum[row1 - 1][col1 - 1]
        blk4 = self.sum[row2][col2]
        return blk4 - blk1 - blk2 + blk3


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        sPtr = 2
        self.res = False
        while not self.res and sPtr < len(num):
            fPtr = 1
            while fPtr < sPtr:
                if (fPtr > 1 and num[0] == '0') or (sPtr - fPtr > 1 and num[fPtr] == '0'):
                    pass
                else:
                    newSeq = [int(num[:fPtr]), int(num[fPtr:sPtr])]
                    newRem = num[sPtr:]
                    self.judgeConstruct(newSeq, newRem)
                fPtr += 1
            sPtr += 1
        return self.res

    def judgeConstruct(self, numSeq, remain):
        if len(remain) > 1 and remain[0] == '0':
            return
        if self.res:
            return
        for length in range(1, len(remain) + 1):
            dic = {}
            curNum = int(remain[:length])
            correct = False
            if curNum == numSeq[-1] + numSeq[-2]:
                correct = True
            '''
                同时判断前面所有数
                for num in numSeq:
                    if curNum < num:
                        continue
                    else:
                        if num not in dic:
                            dic[curNum - num] = 0
                        else:
                            correct = True
            '''

            if correct:
                if length == len(remain):
                    self.res = True
                newSeq = numSeq[:]
                newSeq.append(curNum)
                self.judgeConstruct(newSeq, remain[length:])

    # sell buy with cooldown
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.prices = prices
        self.profitDic = {}
        return self.dp(0)

    def dp(self, pos):
        maxProfit = 0
        while pos < len(self.prices) - 1 and self.prices[pos] > self.prices[pos + 1]:
            pos += 1
        for i in range(pos, len(self.prices)):
            if i + 2 not in self.profitDic:
                self.profitDic[i + 2] = self.dp(i + 2)
            if i + 1 not in self.profitDic:
                self.profitDic[i + 1] = self.dp(i + 1)
            profit = max(self.prices[i] - self.prices[pos] + self.profitDic[i + 2], self.profitDic[i + 1])
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit

    def maxProfitDp2(self, prices):
        profitDic = {}
        profitDic[len(prices)] = 0
        profitDic[len(prices) + 1] = 0
        profitDic[len(prices) - 1] = 0
        for pos in range(len(prices) - 2, -1, -1):
            maxProfit = 0
            for i in range(pos, len(prices)):
                profit = max(prices[i] - prices[pos] + profitDic[i + 2], profitDic[i + 1])
                if profit > maxProfit:
                    maxProfit = profit
            profitDic[pos] = maxProfit
        return profitDic[0]

    def maxProfitState(self, prices):
        # dp1, dp2, dp3 = 0 stock(cool), 0 stock(no-cool), 1 stock(no-cool)
        dp1, dp2, dp3 = 0, 0, -float("inf")
        for p in prices:
            dp1, dp2, dp3 = dp3 + p, max(dp1, dp2), max(dp2 - p, dp3)
        return max(dp1, dp2)

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        nodeDic = {}
        nodeQueue = []
        nextQueue = []
        findAns = False
        Ans = []
        countDic = {}
        for node in range(n):
            countDic[node] = 1
            nodeDic[node] = []
        for edge in edges:
            nodeDic[edge[0]].append(edge[1])
            nodeDic[edge[1]].append(edge[0])
        # format [root,history,cur]
        for node in range(n):
            nodeQueue.append([node, -1, node])
        while nodeQueue:
            cur = nodeQueue.pop()
            for nextNode in nodeDic[cur[2]]:
                if nextNode != cur[1]:
                    nextQueue.append([cur[0], cur[2], nextNode])
                    countDic[cur[0]] += 1
            countDic[cur[0]] -= 1
            if countDic[cur[0]] == 0:
                findAns = True
                Ans.append(cur[0])
            if not nodeQueue:
                if findAns:
                    print(Ans)
                    return Ans
                nodeQueue = nextQueue
                nextQueue = []
        return []

    # Wrong, should check all graph point
    def findMinHeightTrees2(self, n, edges):
        nodeDic = {}
        memoDic = {}
        nodeQueue = []
        nextQueue = []
        removeList = []
        findAns = False
        count = 0
        if n == 1:
            return [0]
        for node in range(n):
            nodeDic[node] = []
            memoDic[node] = []
        for edge in edges:
            nodeDic[edge[0]].append(edge[1])
            nodeDic[edge[1]].append(edge[0])
            memoDic[edge[0]].append(edge[1])
            memoDic[edge[1]].append(edge[0])
            count += 2
        for key, val in nodeDic.items():
            # format [val,hitory,from]
            if len(val) == 1:
                nodeQueue.append([key, -1])
        while nodeQueue:
            cur = nodeQueue.pop()
            countNodeDic = {}
            for nextNode in nodeDic[cur[0]]:
                if nextNode != cur[1]:
                    if cur[0] in nodeDic[nextNode]:
                        removeList.append((nextNode, cur[0]))
                        if cur[0] not in countNodeDic:
                            countNodeDic[cur[0]] = 0
                        else:
                            countNodeDic[cur[0]] += 1
                    nextQueue.append([nextNode, cur[0]])
            if not nodeQueue:
                for remover in removeList:
                    if remover[1] in nodeDic[remover[0]]:
                        nodeDic[remover[0]].remove(remover[1])
                        count -= 1
                        if count == 0:
                            findAns = True
                if findAns:
                    Ans = []
                    center = False
                    for key, val in countNodeDic.items():
                        if val > 0:
                            center = True
                        Ans.append(key)
                    if center:
                        return Ans

                    else:
                        for key in countNodeDic.keys():
                            for val in memoDic[key]:
                                if val in countNodeDic:
                                    Ans.append(val)

                        return Ans
                nodeQueue = nextQueue
                nextQueue = []
                removeList = []

        def findMinHeightTrees(self, n, edges):
            """
            :type n: int
            :type edges: List[List[int]]
            :rtype: List[int]
            """
            if n == 1: return [0]

            graph = [set() for _ in range(n)]
            for i, j in edges:
                graph[i].add(j)
                graph[j].add(i)

            # the intuition is that in a connected graph,
            # if you pick a node of degree 1 as the root
            # then the resulting tree has the max ht.
            # so trim the leaves until there are at most 2
            # and at least 1 node left.

            leaves = [i for i in range(n) if len(graph[i]) == 1]
            while n > 2:
                n -= len(leaves)
                new_leaves = []
                for leaf in leaves:
                    neighbor = graph[leaf].pop()
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) == 1: new_leaves.append(neighbor)

                leaves = new_leaves

            return leaves


print(Solution().findMinHeightTrees2(7, [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]))
# print(Solution().findMinHeightTrees2(909,
# [[0,1],[0,2],[2,3],[0,4],[4,5],[0,6],[6,7],[0,8],[7,9],[1,10],[0,11],[10,12],[8,13],[3,14],[1,15],[1,16],[4,17],[7,18],[15,19],[1,20],[14,21],[9,22],[14,23],[15,24],[7,25],[0,26],[24,27],[13,28],[22,29],[18,30],[18,31],[17,32],[14,33],[20,34],[1,35],[14,36],[14,37],[30,38],[13,39],[6,40],[32,41],[17,42],[23,43],[23,44],[6,45],[27,46],[9,47],[4,48],[16,49],[31,50],[21,51],[21,52],[31,53],[53,54],[18,55],[3,56],[7,57],[52,58],[14,59],[10,60],[20,61],[17,62],[2,63],[36,64],[25,65],[53,66],[61,67],[23,68],[14,69],[29,70],[63,71],[12,72],[6,73],[11,74],[73,75],[60,76],[38,77],[61,78],[71,79],[20,80],[24,81],[60,82],[52,83],[68,84],[22,85],[36,86],[85,87],[9,88],[15,89],[56,90],[16,91],[67,92],[24,93],[63,94],[41,95],[57,96],[83,97],[90,98],[38,99],[54,100],[97,101],[4,102],[51,103],[31,104],[22,105],[102,106],[95,107],[71,108],[9,109],[53,110],[62,111],[110,112],[5,113],[27,114],[104,115],[35,116],[14,117],[0,118],[106,119],[37,120],[8,121],[26,122],[87,123],[49,124],[74,125],[61,126],[17,127],[89,128],[58,129],[33,130],[36,131],[50,132],[43,133],[121,134],[32,135],[113,136],[64,137],[73,138],[13,139],[133,140],[89,141],[36,142],[86,143],[117,144],[11,145],[70,146],[98,147],[82,148],[28,149],[61,150],[66,151],[59,152],[51,153],[49,154],[61,155],[76,156],[155,157],[57,158],[112,159],[19,160],[60,161],[88,162],[62,163],[52,164],[126,165],[48,166],[47,167],[136,168],[15,169],[7,170],[85,171],[61,172],[110,173],[81,174],[135,175],[60,176],[95,177],[171,178],[161,179],[44,180],[19,181],[175,182],[107,183],[23,184],[66,185],[122,186],[128,187],[147,188],[139,189],[135,190],[19,191],[103,192],[51,193],[158,194],[99,195],[75,196],[4,197],[26,198],[131,199],[167,200],[83,201],[131,202],[55,203],[32,204],[164,205],[98,206],[86,207],[170,208],[170,209],[188,210],[40,211],[46,212],[31,213],[18,214],[116,215],[13,216],[212,217],[148,218],[88,219],[19,220],[81,221],[137,222],[23,223],[58,224],[163,225],[145,226],[116,227],[45,228],[31,229],[47,230],[66,231],[82,232],[59,233],[229,234],[164,235],[122,236],[31,237],[143,238],[178,239],[32,240],[97,241],[89,242],[117,243],[191,244],[76,245],[25,246],[217,247],[106,248],[37,249],[12,250],[47,251],[163,252],[247,253],[253,254],[19,255],[245,256],[67,257],[108,258],[50,259],[115,260],[67,261],[248,262],[148,263],[149,264],[220,265],[54,266],[134,267],[2,268],[161,269],[265,270],[31,271],[83,272],[162,273],[267,274],[21,275],[72,276],[26,277],[112,278],[268,279],[41,280],[84,281],[196,282],[281,283],[109,284],[118,285],[66,286],[167,287],[142,288],[154,289],[262,290],[158,291],[216,292],[26,293],[30,294],[60,295],[276,296],[72,297],[215,298],[7,299],[69,300],[289,301],[54,302],[210,303],[280,304],[204,305],[186,306],[217,307],[305,308],[225,309],[13,310],[3,311],[110,312],[82,313],[155,314],[22,315],[66,316],[223,317],[252,318],[229,319],[247,320],[231,321],[190,322],[308,323],[26,324],[245,325],[123,326],[91,327],[308,328],[17,329],[78,330],[136,331],[7,332],[146,333],[318,334],[273,335],[161,336],[35,337],[241,338],[282,339],[133,340],[136,341],[8,342],[146,343],[117,344],[15,345],[102,346],[52,347],[21,348],[166,349],[131,350],[178,351],[142,352],[7,353],[255,354],[346,355],[162,356],[16,357],[253,358],[285,359],[23,360],[7,361],[96,362],[128,363],[231,364],[223,365],[275,366],[347,367],[244,368],[203,369],[55,370],[182,371],[170,372],[270,373],[315,374],[85,375],[346,376],[212,377],[102,378],[319,379],[252,380],[264,381],[351,382],[164,383],[233,384],[361,385],[175,386],[230,387],[331,388],[57,389],[119,390],[118,391],[251,392],[306,393],[255,394],[199,395],[238,396],[17,397],[197,398],[151,399],[356,400],[395,401],[191,402],[16,403],[13,404],[110,405],[313,406],[340,407],[161,408],[301,409],[44,410],[364,411],[272,412],[100,413],[312,414],[307,415],[347,416],[374,417],[187,418],[328,419],[118,420],[311,421],[321,422],[108,423],[395,424],[190,425],[299,426],[79,427],[68,428],[240,429],[386,430],[371,431],[5,432],[255,433],[320,434],[376,435],[81,436],[68,437],[54,438],[421,439],[423,440],[311,441],[41,442],[3,443],[400,444],[137,445],[253,446],[335,447],[376,448],[1,449],[212,450],[169,451],[383,452],[401,453],[383,454],[54,455],[59,456],[35,457],[121,458],[173,459],[388,460],[456,461],[81,462],[368,463],[219,464],[178,465],[114,466],[384,467],[104,468],[268,469],[170,470],[246,471],[319,472],[258,473],[326,474],[241,475],[25,476],[468,477],[444,478],[418,479],[405,480],[261,481],[447,482],[140,483],[30,484],[375,485],[75,486],[455,487],[64,488],[236,489],[454,490],[207,491],[431,492],[290,493],[84,494],[409,495],[315,496],[343,497],[480,498],[451,499],[155,500],[262,501],[111,502],[441,503],[237,504],[387,505],[275,506],[75,507],[259,508],[465,509],[433,510],[217,511],[450,512],[30,513],[479,514],[179,515],[102,516],[181,517],[153,518],[208,519],[380,520],[256,521],[276,522],[253,523],[417,524],[179,525],[305,526],[450,527],[407,528],[442,529],[99,530],[381,531],[89,532],[507,533],[347,534],[132,535],[445,536],[197,537],[255,538],[479,539],[322,540],[277,541],[342,542],[44,543],[443,544],[322,545],[96,546],[397,547],[195,548],[316,549],[13,550],[397,551],[405,552],[250,553],[365,554],[108,555],[213,556],[97,557],[406,558],[156,559],[421,560],[80,561],[328,562],[303,563],[243,564],[269,565],[485,566],[457,567],[371,568],[201,569],[337,570],[183,571],[221,572],[113,573],[447,574],[244,575],[429,576],[126,577],[69,578],[535,579],[303,580],[283,581],[567,582],[209,583],[21,584],[227,585],[21,586],[16,587],[268,588],[45,589],[107,590],[141,591],[40,592],[157,593],[328,594],[68,595],[225,596],[219,597],[301,598],[44,599],[515,600],[334,601],[229,602],[95,603],[177,604],[408,605],[119,606],[200,607],[334,608],[142,609],[437,610],[391,611],[272,612],[231,613],[566,614],[64,615],[186,616],[584,617],[9,618],[369,619],[21,620],[477,621],[17,622],[604,623],[228,624],[225,625],[615,626],[403,627],[90,628],[459,629],[171,630],[52,631],[626,632],[385,633],[96,634],[120,635],[161,636],[86,637],[14,638],[302,639],[402,640],[191,641],[355,642],[475,643],[267,644],[616,645],[10,646],[595,647],[295,648],[332,649],[78,650],[334,651],[402,652],[215,653],[328,654],[383,655],[461,656],[608,657],[590,658],[427,659],[115,660],[301,661],[579,662],[361,663],[602,664],[215,665],[181,666],[292,667],[126,668],[160,669],[640,670],[559,671],[301,672],[221,673],[226,674],[430,675],[403,676],[484,677],[395,678],[659,679],[169,680],[627,681],[48,682],[421,683],[589,684],[100,685],[662,686],[244,687],[440,688],[623,689],[626,690],[46,691],[148,692],[688,693],[87,694],[635,695],[609,696],[186,697],[317,698],[654,699],[412,700],[291,701],[481,702],[639,703],[596,704],[40,705],[382,706],[222,707],[445,708],[409,709],[612,710],[214,711],[658,712],[363,713],[399,714],[335,715],[274,716],[21,717],[109,718],[232,719],[551,720],[113,721],[78,722],[20,723],[172,724],[192,725],[291,726],[47,727],[378,728],[372,729],[349,730],[696,731],[362,732],[509,733],[603,734],[481,735],[633,736],[709,737],[610,738],[671,739],[525,740],[176,741],[329,742],[451,743],[23,744],[190,745],[473,746],[234,747],[470,748],[160,749],[599,750],[50,751],[176,752],[69,753],[525,754],[97,755],[692,756],[117,757],[364,758],[627,759],[393,760],[415,761],[222,762],[737,763],[461,764],[392,765],[28,766],[663,767],[274,768],[673,769],[607,770],[160,771],[222,772],[605,773],[342,774],[418,775],[269,776],[371,777],[235,778],[299,779],[725,780],[297,781],[233,782],[260,783],[214,784],[247,785],[170,786],[517,787],[612,788],[246,789],[52,790],[173,791],[490,792],[297,793],[451,794],[309,795],[65,796],[352,797],[178,798],[403,799],[338,800],[342,801],[282,802],[317,803],[361,804],[479,805],[141,806],[280,807],[303,808],[265,809],[172,810],[42,811],[39,812],[133,813],[339,814],[744,815],[765,816],[165,817],[323,818],[238,819],[95,820],[76,821],[37,822],[283,823],[410,824],[464,825],[666,826],[23,827],[669,828],[77,829],[512,830],[739,831],[813,832],[342,833],[18,834],[354,835],[641,836],[318,837],[480,838],[287,839],[521,840],[29,841],[224,842],[9,843],[119,844],[47,845],[291,846],[239,847],[249,848],[448,849],[347,850],[380,851],[354,852],[473,853],[55,854],[413,855],[635,856],[350,857],[454,858],[80,859],[550,860],[361,861],[660,862],[427,863],[535,864],[317,865],[162,866],[427,867],[732,868],[4,869],[611,870],[771,871],[311,872],[600,873],[809,874],[634,875],[618,876],[123,877],[373,878],[600,879],[686,880],[610,881],[361,882],[108,883],[397,884],[766,885],[440,886],[434,887],[627,888],[263,889],[316,890],[651,891],[668,892],[119,893],[696,894],[624,895],[133,896],[228,897],[71,898],[162,899],[496,900],[749,901],[802,902],[471,903],[117,904],[84,905],[212,906],[42,907],[351,908]]))


print(Solution().findMinHeightTrees2(7, [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]))
# print(Solution().findMinHeightTrees2(909,
# [[0,1],[0,2],[2,3],[0,4],[4,5],[0,6],[6,7],[0,8],[7,9],[1,10],[0,11],[10,12],[8,13],[3,14],[1,15],[1,16],[4,17],[7,18],[15,19],[1,20],[14,21],[9,22],[14,23],[15,24],[7,25],[0,26],[24,27],[13,28],[22,29],[18,30],[18,31],[17,32],[14,33],[20,34],[1,35],[14,36],[14,37],[30,38],[13,39],[6,40],[32,41],[17,42],[23,43],[23,44],[6,45],[27,46],[9,47],[4,48],[16,49],[31,50],[21,51],[21,52],[31,53],[53,54],[18,55],[3,56],[7,57],[52,58],[14,59],[10,60],[20,61],[17,62],[2,63],[36,64],[25,65],[53,66],[61,67],[23,68],[14,69],[29,70],[63,71],[12,72],[6,73],[11,74],[73,75],[60,76],[38,77],[61,78],[71,79],[20,80],[24,81],[60,82],[52,83],[68,84],[22,85],[36,86],[85,87],[9,88],[15,89],[56,90],[16,91],[67,92],[24,93],[63,94],[41,95],[57,96],[83,97],[90,98],[38,99],[54,100],[97,101],[4,102],[51,103],[31,104],[22,105],[102,106],[95,107],[71,108],[9,109],[53,110],[62,111],[110,112],[5,113],[27,114],[104,115],[35,116],[14,117],[0,118],[106,119],[37,120],[8,121],[26,122],[87,123],[49,124],[74,125],[61,126],[17,127],[89,128],[58,129],[33,130],[36,131],[50,132],[43,133],[121,134],[32,135],[113,136],[64,137],[73,138],[13,139],[133,140],[89,141],[36,142],[86,143],[117,144],[11,145],[70,146],[98,147],[82,148],[28,149],[61,150],[66,151],[59,152],[51,153],[49,154],[61,155],[76,156],[155,157],[57,158],[112,159],[19,160],[60,161],[88,162],[62,163],[52,164],[126,165],[48,166],[47,167],[136,168],[15,169],[7,170],[85,171],[61,172],[110,173],[81,174],[135,175],[60,176],[95,177],[171,178],[161,179],[44,180],[19,181],[175,182],[107,183],[23,184],[66,185],[122,186],[128,187],[147,188],[139,189],[135,190],[19,191],[103,192],[51,193],[158,194],[99,195],[75,196],[4,197],[26,198],[131,199],[167,200],[83,201],[131,202],[55,203],[32,204],[164,205],[98,206],[86,207],[170,208],[170,209],[188,210],[40,211],[46,212],[31,213],[18,214],[116,215],[13,216],[212,217],[148,218],[88,219],[19,220],[81,221],[137,222],[23,223],[58,224],[163,225],[145,226],[116,227],[45,228],[31,229],[47,230],[66,231],[82,232],[59,233],[229,234],[164,235],[122,236],[31,237],[143,238],[178,239],[32,240],[97,241],[89,242],[117,243],[191,244],[76,245],[25,246],[217,247],[106,248],[37,249],[12,250],[47,251],[163,252],[247,253],[253,254],[19,255],[245,256],[67,257],[108,258],[50,259],[115,260],[67,261],[248,262],[148,263],[149,264],[220,265],[54,266],[134,267],[2,268],[161,269],[265,270],[31,271],[83,272],[162,273],[267,274],[21,275],[72,276],[26,277],[112,278],[268,279],[41,280],[84,281],[196,282],[281,283],[109,284],[118,285],[66,286],[167,287],[142,288],[154,289],[262,290],[158,291],[216,292],[26,293],[30,294],[60,295],[276,296],[72,297],[215,298],[7,299],[69,300],[289,301],[54,302],[210,303],[280,304],[204,305],[186,306],[217,307],[305,308],[225,309],[13,310],[3,311],[110,312],[82,313],[155,314],[22,315],[66,316],[223,317],[252,318],[229,319],[247,320],[231,321],[190,322],[308,323],[26,324],[245,325],[123,326],[91,327],[308,328],[17,329],[78,330],[136,331],[7,332],[146,333],[318,334],[273,335],[161,336],[35,337],[241,338],[282,339],[133,340],[136,341],[8,342],[146,343],[117,344],[15,345],[102,346],[52,347],[21,348],[166,349],[131,350],[178,351],[142,352],[7,353],[255,354],[346,355],[162,356],[16,357],[253,358],[285,359],[23,360],[7,361],[96,362],[128,363],[231,364],[223,365],[275,366],[347,367],[244,368],[203,369],[55,370],[182,371],[170,372],[270,373],[315,374],[85,375],[346,376],[212,377],[102,378],[319,379],[252,380],[264,381],[351,382],[164,383],[233,384],[361,385],[175,386],[230,387],[331,388],[57,389],[119,390],[118,391],[251,392],[306,393],[255,394],[199,395],[238,396],[17,397],[197,398],[151,399],[356,400],[395,401],[191,402],[16,403],[13,404],[110,405],[313,406],[340,407],[161,408],[301,409],[44,410],[364,411],[272,412],[100,413],[312,414],[307,415],[347,416],[374,417],[187,418],[328,419],[118,420],[311,421],[321,422],[108,423],[395,424],[190,425],[299,426],[79,427],[68,428],[240,429],[386,430],[371,431],[5,432],[255,433],[320,434],[376,435],[81,436],[68,437],[54,438],[421,439],[423,440],[311,441],[41,442],[3,443],[400,444],[137,445],[253,446],[335,447],[376,448],[1,449],[212,450],[169,451],[383,452],[401,453],[383,454],[54,455],[59,456],[35,457],[121,458],[173,459],[388,460],[456,461],[81,462],[368,463],[219,464],[178,465],[114,466],[384,467],[104,468],[268,469],[170,470],[246,471],[319,472],[258,473],[326,474],[241,475],[25,476],[468,477],[444,478],[418,479],[405,480],[261,481],[447,482],[140,483],[30,484],[375,485],[75,486],[455,487],[64,488],[236,489],[454,490],[207,491],[431,492],[290,493],[84,494],[409,495],[315,496],[343,497],[480,498],[451,499],[155,500],[262,501],[111,502],[441,503],[237,504],[387,505],[275,506],[75,507],[259,508],[465,509],[433,510],[217,511],[450,512],[30,513],[479,514],[179,515],[102,516],[181,517],[153,518],[208,519],[380,520],[256,521],[276,522],[253,523],[417,524],[179,525],[305,526],[450,527],[407,528],[442,529],[99,530],[381,531],[89,532],[507,533],[347,534],[132,535],[445,536],[197,537],[255,538],[479,539],[322,540],[277,541],[342,542],[44,543],[443,544],[322,545],[96,546],[397,547],[195,548],[316,549],[13,550],[397,551],[405,552],[250,553],[365,554],[108,555],[213,556],[97,557],[406,558],[156,559],[421,560],[80,561],[328,562],[303,563],[243,564],[269,565],[485,566],[457,567],[371,568],[201,569],[337,570],[183,571],[221,572],[113,573],[447,574],[244,575],[429,576],[126,577],[69,578],[535,579],[303,580],[283,581],[567,582],[209,583],[21,584],[227,585],[21,586],[16,587],[268,588],[45,589],[107,590],[141,591],[40,592],[157,593],[328,594],[68,595],[225,596],[219,597],[301,598],[44,599],[515,600],[334,601],[229,602],[95,603],[177,604],[408,605],[119,606],[200,607],[334,608],[142,609],[437,610],[391,611],[272,612],[231,613],[566,614],[64,615],[186,616],[584,617],[9,618],[369,619],[21,620],[477,621],[17,622],[604,623],[228,624],[225,625],[615,626],[403,627],[90,628],[459,629],[171,630],[52,631],[626,632],[385,633],[96,634],[120,635],[161,636],[86,637],[14,638],[302,639],[402,640],[191,641],[355,642],[475,643],[267,644],[616,645],[10,646],[595,647],[295,648],[332,649],[78,650],[334,651],[402,652],[215,653],[328,654],[383,655],[461,656],[608,657],[590,658],[427,659],[115,660],[301,661],[579,662],[361,663],[602,664],[215,665],[181,666],[292,667],[126,668],[160,669],[640,670],[559,671],[301,672],[221,673],[226,674],[430,675],[403,676],[484,677],[395,678],[659,679],[169,680],[627,681],[48,682],[421,683],[589,684],[100,685],[662,686],[244,687],[440,688],[623,689],[626,690],[46,691],[148,692],[688,693],[87,694],[635,695],[609,696],[186,697],[317,698],[654,699],[412,700],[291,701],[481,702],[639,703],[596,704],[40,705],[382,706],[222,707],[445,708],[409,709],[612,710],[214,711],[658,712],[363,713],[399,714],[335,715],[274,716],[21,717],[109,718],[232,719],[551,720],[113,721],[78,722],[20,723],[172,724],[192,725],[291,726],[47,727],[378,728],[372,729],[349,730],[696,731],[362,732],[509,733],[603,734],[481,735],[633,736],[709,737],[610,738],[671,739],[525,740],[176,741],[329,742],[451,743],[23,744],[190,745],[473,746],[234,747],[470,748],[160,749],[599,750],[50,751],[176,752],[69,753],[525,754],[97,755],[692,756],[117,757],[364,758],[627,759],[393,760],[415,761],[222,762],[737,763],[461,764],[392,765],[28,766],[663,767],[274,768],[673,769],[607,770],[160,771],[222,772],[605,773],[342,774],[418,775],[269,776],[371,777],[235,778],[299,779],[725,780],[297,781],[233,782],[260,783],[214,784],[247,785],[170,786],[517,787],[612,788],[246,789],[52,790],[173,791],[490,792],[297,793],[451,794],[309,795],[65,796],[352,797],[178,798],[403,799],[338,800],[342,801],[282,802],[317,803],[361,804],[479,805],[141,806],[280,807],[303,808],[265,809],[172,810],[42,811],[39,812],[133,813],[339,814],[744,815],[765,816],[165,817],[323,818],[238,819],[95,820],[76,821],[37,822],[283,823],[410,824],[464,825],[666,826],[23,827],[669,828],[77,829],[512,830],[739,831],[813,832],[342,833],[18,834],[354,835],[641,836],[318,837],[480,838],[287,839],[521,840],[29,841],[224,842],[9,843],[119,844],[47,845],[291,846],[239,847],[249,848],[448,849],[347,850],[380,851],[354,852],[473,853],[55,854],[413,855],[635,856],[350,857],[454,858],[80,859],[550,860],[361,861],[660,862],[427,863],[535,864],[317,865],[162,866],[427,867],[732,868],[4,869],[611,870],[771,871],[311,872],[600,873],[809,874],[634,875],[618,876],[123,877],[373,878],[600,879],[686,880],[610,881],[361,882],[108,883],[397,884],[766,885],[440,886],[434,887],[627,888],[263,889],[316,890],[651,891],[668,892],[119,893],[696,894],[624,895],[133,896],[228,897],[71,898],[162,899],[496,900],[749,901],[802,902],[471,903],[117,904],[84,905],[212,906],[42,907],[351,908]]))
