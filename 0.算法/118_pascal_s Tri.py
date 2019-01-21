class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            sub_list = []
            if i == 0:
                sub_list = [1]
            else:
                for j in range(len(result[-1])+1):
                    if j == 0 or j == len(result[-1]):
                        sub_list.append(1)
                    else:
                        sub_list.append(result[-1][j-1]+result[-1][j])
            result.append(sub_list)
        return result

a = Solution()
print(a.generate(5))