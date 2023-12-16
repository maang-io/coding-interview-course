#
from collections import deque


class Solution(object):
    def closestNode(self, n, edges, query):
        """
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """
        graph = dict() # adj list representation
        for i in range(n):
            graph.update({i: []})
        
        def buildGraph():
            for edge in edges:
                u,v = edge[0], edge[1]
                # it is bidirectional edge
                graph[u].append(v)
                graph[v].append(u)
        def dfs(cur, dest, path):
            # visit this 
            path.add(cur) 
            if cur == dest:
                return True
            
            # explore nbrs
            nbrs = graph[cur]
            for nbr in nbrs:
                if nbr in path:
                    continue
                found = dfs(nbr,dest,path)
                if found:
                    return True
            path.remove(cur)
            return False
        def bfs_search(node, path):
            q = deque()
            visited = set()
            q.append(node)
            visited.add(node)
            while q:
                cur = q.popleft()
                if cur in path:
                    return cur
                nbrs = graph[cur]
                for nbr in nbrs:
                    if nbr in visited:
                        continue
                    visited.add(nbr)
                    q.append(nbr)
            return -1
        
        buildGraph()
        #print(graph)
        N = len(query)
        result = [-1]*N
        for i in range(N):
            src,dest,node = query[i][0], query[i][1], query[i][2]
            path = set()
            dfs(src,dest,path)
            #print(src,dest, path)
            result[i] = bfs_search(node, path)
        return result
