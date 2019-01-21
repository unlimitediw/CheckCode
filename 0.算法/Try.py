class Solution():
    def a(self):
        return 5 + self.b()
    def b(self):
        return 6 + self.a()


c = Solution()
print(c.a)