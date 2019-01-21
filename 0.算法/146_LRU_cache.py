class LRUCache(object):

    cache = {}
    rank_queue = []
    capacity = 0

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.rank_queue = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        if key in self.rank_queue:
            self.rank_queue.remove(key)
        self.rank_queue.append(key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.cache and len(self.cache) == self.capacity:
            del self.cache[self.rank_queue[0]]
            self.rank_queue.pop(0)
        if key in self.rank_queue:
            self.rank_queue.remove(key)
        self.rank_queue.append(key)
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

dic = {}
dic[1] = 7
dic[2] = 8
dic[3] = 9
del dic[1]
rank_queue = [2,1,3,4]
rank_queue.pop(0)
print(rank_queue)

