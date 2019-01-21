class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """

        line = 1
        length = 0
        for i in range(len(S)):
            add = widths[ord(S[i]) - ord('a')]
            if add + length > 100:
                line += 1
                length = add
            else:
                length += add
        return line, length

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        check_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        diff = {}
        for w in words:
            newW = ''
            for c in w:
                newW += check_list[ord(c) - ord('a')]
            if newW not in diff:
                diff[newW] = 1
        return len(diff)

    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        # check row
        # check col
        rowMemo = [0 for i in range(len(grid))]
        colMemo = [0 for i in range(len(grid[0]))]
        for row in range(len(grid)):
            rowMax = 0
            for col in range(len(grid[row])):
                if grid[row][col] > rowMax:
                    rowMax = grid[row][col]
            rowMemo[row] = rowMax
        for col in range(len(grid[0])):
            colMax = 0
            for row in range(len(grid)):
                if grid[row][col] > colMax:
                    colMax = grid[row][col]
            colMemo[col] = colMax
        diff = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # give new sum
                diff += min(rowMemo[row], colMemo[col])
                # minus original one
                diff -= grid[row][col]
        return diff

    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        b_value = 0
        c_value = 0
        remain_value = 0
        for i in A:
            remain_value += i
        return self.split_sub(A, 0, b_value, c_value, 0, 0)

    def split_sub(self, A, count, b_value, c_value, b_count, c_count):
        if count == len(A):
            if b_count == 0 or c_count == 0:
                return False
            else:
                if b_value/b_count == c_value/c_count:
                    return True
                else:
                    return False
        if b_count != 0 and c_count != 0:
            if b_value / b_count < c_value / c_count:
                if not self.compare_LS(A, count, b_value, c_value, b_count, c_count):
                    return False
            elif b_value / b_count > c_value / c_count:
                if not self.compare_LS(A, count, c_value, b_value, c_count, b_count):
                    return False
        if self.split_sub(A, count + 1, b_value + A[count], c_value, b_count + 1, c_count) or \
                self.split_sub(A, count + 1, b_value, c_value + A[count], b_count, c_count + 1):
            return True
        return False

    def compare_LS(self, A, count, small_value, large_value, small_count, large_count):
        small_average = small_value / small_count
        large_average = large_value / large_count
        for i in A[count:]:
            if i < small_average:
                large_value += i
                large_count += 1
                large_average = large_value / large_count
            elif i >= large_average:
                small_value += i
                small_count += 1
                small_average = small_value/small_count
            if small_value / small_count >= large_value / large_count:
                return True
        return False


T = Solution()
print(T.splitArraySameAverage([33,86,88,78,21,76,19,20,88,76,10,25,37,97,58,89,65,59,98,57,50,30,58,5,61,72,23,6]))
