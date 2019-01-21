class Solution(object):
    def TtrailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        total1 = 1
        total2 = 1
        count = 0
        count2 = 0
        newN = n
        while newN > 0:
            total1 *= newN
            newN -= 1
            if total1 % 10 == 0:
                count += 1
                total1 //= 10
        while n > 0:
            total2 *= n
            n -= 1

        print(total2)
        while total2 > 9:
            if total2 % 10 == 0:
                count2 += 1
            else:
                break
            total2 //= 10


        return count, count2

    def trailingZeroes(self, n):
        level = 0
        k = n
        count = 1
        if n < 5:
            return 0
        while k // 5 > 0:
            level += 1
            if level == 1:
                count = 1
            else:
                count = count * 5 + 1
            k //= 5
        return self.trailingZeros(n - 5**level) + count


print(Solution().trailingZeros(30))
