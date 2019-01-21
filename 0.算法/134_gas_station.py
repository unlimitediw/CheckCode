class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        k = []
        remain = 0
        start = 0
        idx = 0
        for i in range(len(gas)):
            k.append(gas[i] - cost[i])
        while True:
            if start < len(k):
                remain += k[idx % len(k)]
                if remain < 0:
                    start = idx + 1
                    remain = 0
                elif idx - start == len(k) - 1:
                    return start
            else:
                return -1
            idx += 1


a = Solution()
print(a.canCompleteCircuit([1, 2], [2, 1]))
