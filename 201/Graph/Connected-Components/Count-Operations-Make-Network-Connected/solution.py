
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
class Solution(object):
    def makeConnected(self, N, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < N-1:
            return -1

        def buildGraph():
            graph = dict()
            for conn in connections:
                u,v = conn
                if u not in graph:
                    graph[u] = []
                graph[u].append(v)

                if v not in graph:
                    graph[v] = []
                graph[v].append(u)
            return graph

        def dfs(cur):
            #visit
            visited.add(cur)

            #explore nbrs
            if cur not in graph:
                return
            nbrs = graph[cur]
            for nbr in nbrs:
                if nbr in visited:
                    continue
                dfs(nbr)

        visited = set()
        count = 0
        graph = buildGraph()
        for cur in range(N) :
            if cur in visited:
                continue
            dfs(cur)
            count+=1
        
        return count-1