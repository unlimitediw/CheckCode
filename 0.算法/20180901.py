class Solution(object):
    def minDistance(self,word1,word2):
        dic = {}
        len1, len2 = len(word1),len(word2)
        def Dfs(pos1,pos2):
            if pos1 == len1 or pos2 == len2:
                return max(len1-pos1,len2-pos2)
            hash = (pos1,pos2)
            if hash not in dic:
                if word1[pos1] == word2[pos2]:
                    dic[hash] = Dfs(pos1+1,pos2+1)
                else:
                    dic[hash] = 1 + min(Dfs(pos1+1,pos2),Dfs(pos1,pos2+1))
            return dic[hash]
        return Dfs(0,0)


print(Solution().minDistance("dinitrophenylhydrazine",
                "acetylphenylhydrazine"))