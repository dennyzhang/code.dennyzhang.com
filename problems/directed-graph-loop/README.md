
# LintCode: Directed Graph Loop     :BLOG:Basic:

---

Directed Graph Loop  

---

Similar Problems:  

-   [Review: BFS Problems](https://code.dennyzhang.com/review-bfs)
-   Tag: [#classic](https://code.dennyzhang.com/tag/classic), [#bfs](https://code.dennyzhang.com/tag/bfs)

---

Please judge whether there is a cycle in the directed graph with n vertices and m edges. The parameter is two int arrays. There is a directed edge from start[i] to end[i].  

Notice  

-   2 <= n <= 10^5
-   1 <= m <= 4\*10^5
-   1 <= start[i], end[i] <= n

Example  

    Given start = [1],end = [2], return "False".
    
    Explanation:
    There is only one edge 1->2, and do not form a cycle.

    Given start = [1,2,3],end = [2,3,1], return "True".
    
    Explanation:
    There is a cycle 1->2->3->1.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/directed-graph-loop)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/directed-graph-loop/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/directed-graph-loop
    class Solution:
        """
        @param start: The start points set
        @param end: The end points set
        @return: Return if the graph is cyclic
        """
        def isCyclicGraph(self, start, end):
    	## Basic Ideas: hashmap
    	##   Keep adding related edge, if we visit one node twice. It's a loop
    	## Complexity: Time O(n), Space O(n)
    	import collections
    	m = collections.defaultdict(lambda: [])
    	edge_count = len(start)
    	global_seen = set([])
    
    	visits = [False for i in range(edge_count)]
    	for i in range(edge_count):
    	    m[start[i]].append(end[i])
    
    	for i in range(edge_count):
    	    if start[i] not in global_seen:
    		queue = collections.deque()
    		seen = set([])
    		queue.append(start[i])
    		seen.add(start[i])
    
    		global_seen.add(start[i])
    		while len(queue) != 0:
    		    for k in range(len(queue)):
    			node = queue.popleft()
    			for node2 in m[node]:
    			    if node2 in seen: return True
    			    queue.append(node2)
    			    seen.add(node2)
    			    global_seen.add(node2)
    	return False

