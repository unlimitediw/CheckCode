class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        #Astar
        dic = {}
        for word in wordList:
            dic[word] = self.wordDistance(word,endWord)

        #BFS
        wordQueue = []
        for word in wordList:
            if self.checkOneWord(beginWord,word):
                wordQueue.append(word)
                del wordList[word]
        while wordQueue:
            currentWord = wordQueue.pop(0)
            for word in wordList:
                if self.checkOneWord(currentWord,word):
                    if word == endWord:
                        wordQueue.append(word)
                    del wordList[word]



    def wordDistance(self,wordA,wordB):
        count = 0
        for i in range(len(wordA)):
            if wordA[i] != wordB[i]:
                count+= 1
        return count

    def checkOneWord(self,wordA,wordB):
        count = 0
        for i in range(len(wordA)):
            if wordA[i] != wordB[i]:
                count+= 1
            if count > 1:
                return False
        if count == 1:
            return True
        else:
            return False