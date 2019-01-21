class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)
        if total % 2 == 1:
            return False
        halfTarget = total / 2
        nums = sorted(nums)
        dic = {}

        def findTarget(startPos, target):
            if (startPos, target) in dic:
                return dic[(startPos, target)]
            for i in range(startPos, len(nums)):
                if nums[i] == target:
                    return True
                elif nums[i] > target:
                    break
                else:
                    if findTarget(i + 1, target - nums[i]):
                        return True
            dic[(startPos, target)] = False
            return False

        return findTarget(0, halfTarget)

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # 0 both can not, 1 paci, 2 atlantic, 3 both can
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        if not matrix:
            return []
        res = []
        for i in range(len(dp)):
            dp[i][0] = 1
            dp[i][-1] = 2
        for i in range(len(dp[0])):
            dp[0][i] = 1
            dp[-1][i] = 2
        if len(matrix[0]) > 1 and len(matrix) > 1:
            dp[0][-1] = 3
            dp[-1][0] = 3
            res = [[0, len(matrix[0]) - 1], [len(matrix) - 1, 0]]

        def check(pos, dir):
            if pos[0] < 0 or pos[0] >= len(matrix) or pos[1] <0 or pos[1] >= len(matrix[0]):
                return
            if dp[pos[0]][pos[1]] == 3:
                return
            if pos[0] - dir >= 0 and pos[0] - dir < len(matrix):
                if matrix[pos[0]][pos[1]] >= matrix[pos[0] - dir][pos[1]]:
                    if dp[pos[0]][pos[1]] == 0:
                        dp[pos[0]][pos[1]] = dp[pos[0] - dir][pos[1]]
                    elif dp[pos[0]][pos[1]] + dp[pos[0] - dir][pos[1]] >= 3 and dp[pos[0]][pos[1]] != dp[pos[0] - dir][
                        pos[1]]:
                        dp[pos[0]][pos[1]] = 3
                    if dp[pos[0]][pos[1]] == 3:
                        res.append([pos[0], pos[1]])
                        return
            if pos[1] - dir >= 0 and pos[1] - dir < len(matrix[0]):
                if matrix[pos[0]][pos[1]] >= matrix[pos[0]][pos[1] - dir]:
                    if dp[pos[0]][pos[1]] == 0:
                        dp[pos[0]][pos[1]] = dp[pos[0]][pos[1] - dir]
                    elif dp[pos[0]][pos[1]] + dp[pos[0]][pos[1] - dir] >= 3 and dp[pos[0]][pos[1]] != dp[pos[0]][
                        pos[1] - dir]:
                        dp[pos[0]][pos[1]] = 3
                    if dp[pos[0]][pos[1]] == 3:
                        res.append([pos[0], pos[1]])

        largerLength = max(len(matrix[0]), len(matrix))
        for i in range(0,largerLength):
            k = 0
            while k <= i:
                check([i - k, k], 1)
                k += 1
        for i in range(1,largerLength):
            k = 0
            while k <= largerLength - 1 -i:
                check([i + k, len(matrix) - 1 - k], 1)
                k += 1
        for i in range(largerLength - 1, -1, -1):
            k = 0
            while k <= largerLength - 1 - i:
                check([i + k, len(matrix) - 1 - k], -1)
                k += 1
        for i in range(largerLength - i - 2, -1, -1):
            k = 0
            while k <= i:
                check([i - k, k], -1)
                k += 1
        return res


    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        '''
                if len(board) == 1 and len(board[0]) == 1 and board[0][0] == 'X':
            return 1
        '''

        res = 0
        for i in range(len(board)):
            cur = 0
            state = 0
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    state = 0
                    cur = 0
                elif state == 0:
                    if i == 0 and i < len(board) - 1 and len(board) >= 2:
                        if board[1][j] == 'X':
                            state = 1
                        else:
                            state = 0
                    elif i == len(board) -1 and i >0 and len(board) >= 2:
                        if board[-2][j] == 'X':
                            state = 1
                        else:
                            state = 0
                    elif i > 0 and i < len(board) - 1 and len(board) >=3:
                        if board[i+1][j] == 'X' or board[i-1][j] == 'X':
                            state = 1
                        else:
                            state = 0
                    if state == 1:
                        res -= 1
                    if cur == 0:
                        res += 1
                    cur = 1
        print(res)
        for i in range(len(board[0])):
            cur = 0
            state = 0
            for j in range(len(board)):
                if board[j][i] == '.':
                    state = 0
                    cur = 0
                else:
                    if state == 0:
                        if i == 0 and i < len(board[0]) - 1 and len(board[0]) >= 2:
                            if board[j][1] == 'X':
                                state = 1
                            else:
                                state = 0
                        elif i == len(board[0]) -1 and i >0 and len(board[0]) >= 2:
                            if board[j][-2] == 'X':
                                state = 1
                            else:
                                state = 0
                        elif 0 < i < len(board[0]) - 1 and len(board[0]) >= 3:
                            if board[j][i+1] == 'X' or board[j][i-1] == 'X':
                                state = 1
                            else:
                                state = 0
                        if state == 1:
                            res -= 1
                        if cur == 0:
                            res += 1
                        cur = 1
        def checkFour(pos):
            for newPos in [[pos[0]+1,pos[1]],[pos[0]-1,pos[1]],[pos[0],pos[1]+1],[pos[0],pos[1]-1]]:
                if 0 <= newPos[0] < len(board) and 0 <= newPos[1] < len(board[0]):
                    if board[newPos[0]][newPos[1]] == 'X':
                        return False
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and checkFour([i,j]):
                    res -= 1
        return res


print(Solution().countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))