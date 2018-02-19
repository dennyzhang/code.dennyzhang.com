# Leetcode: Is Graph Bipartite?     :BLOG:Medium:


---

Is Graph Bipartite?  

---

Similar Problems:  
-   Tag: [#bfs](https://brain.dennyzhang.com/tag/bfs)
-   Tag: [#inspiring](https://brain.dennyzhang.com/tag/inspiring)

---

Given a graph, return true if and only if it is bipartite.  

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.  

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.  

    Example 1:
    Input: [[1,3], [0,2], [1,3], [0,2]]
    Output: true
    Explanation: 
    The graph looks like this:
    0----1
    |    |
    |    |
    3----2
    We can divide the vertices into two groups: {0, 2} and {1, 3}.

    Example 2:
    Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
    Output: false
    Explanation: 
    The graph looks like this:
    0----1
    | \  |
    |  \ |
    3----2
    
    We cannot find a way to divide the set of nodes into two independent subsets.

Note:  

-   graph will have length in range [1, 100].
-   graph[i] will contain integers in range [0, graph.length - 1].
-   graph[i] will not contain i or duplicate values.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/is-graph-bipartite)  

Credits To: [leetcode.com](https://leetcode.com/problems/is-graph-bipartite/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/is-graph-bipartite
    class Solution:
        ## Basic Ideas: DFS
        ##
        ## Complexity: Time O(n), Space O(n)
        def isBipartite(self, graph):
            """
            :type graph: List[List[int]]
            :rtype: bool
            """
            length = len(graph)
            self.set_type = [0]*length
            for i in range(length):
                if self.set_type[i] == 0:
                    # start dfs
                    if self.dfs(graph, i, 1) is False:
                        return False
            return True
    
        def dfs(self, graph, node, type):
            # mark current node
            self.set_type[node] = type
    
            # check the neighbors of current node
            for edge in graph[node]:
                if self.set_type[edge] == 0:
                    if self.dfs(graph, edge, -type) is False:
                        return False
                elif self.set_type[edge] == type:
                    return False
            return True
    
        ## Basic Ideas: BFS
        ## 
        ##      With one BFS, all connected nodes in current forest will be visited
        ##      For two forests, we can put the first nodes into the same set.
        ##      This is a key improvement, compared to brutple force 
        ##
        ##      set_type[]: [0, 1, -1], [undecided, type1, type2]
        ##
        ## Complexity: Time O(n), Space O(n)
        def isBipartite_v1(self, graph):
            """
            :type graph: List[List[int]]
            :rtype: bool
            """
            import collections
            length = len(graph)
            set_type = [0]*length
            for i in range(length):
                # a new forest starts
                if set_type[i] == 0:
                    set_type[i] = 1
                    queue = collections.deque()
                    queue.append((i, 1))
                    # BFS
                    while len(queue) != 0:
                        for k in range(len(queue)):
                            (node, node_type) = queue.popleft()
                            # find the neighbors
                            for edge in graph[node]:
                                if set_type[edge] == 0:
                                    # get the candidates
                                    set_type[edge] = -node_type
                                    queue.append((edge, -node_type))
                                elif set_type[edge] == node_type:
                                    # detect a conflict
                                    return False
            return True