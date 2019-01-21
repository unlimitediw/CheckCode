class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        ans = [1]
        for i in range(1, (rowIndex + 2) // 2):
            ans.append(ans[i - 1] * (rowIndex - i + 1) // i)

        if rowIndex % 2 == 0:
            return ans + ans[:-1][::-1]
        else:
            return ans + ans[::-1]