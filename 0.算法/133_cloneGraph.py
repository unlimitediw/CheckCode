# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        memo = {}
        def clone(node):
            if node not in memo:
                c = memo[node] = UndirectedGraphNode(node.label)
                c.neighbors = map(clone,node.neighbors)
            return memo[node]
        return node and clone(node)