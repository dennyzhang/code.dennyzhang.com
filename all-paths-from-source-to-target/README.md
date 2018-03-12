Smallest Rotation with Highest Score\* Leetcode: All Paths From Source to Target                      :BLOG:Basic:  


---

All Paths From Source to Target  

---

Similar Problems:  
-   [Is Graph Bipartite](https://brain.dennyzhang.com/is-graph-bipartite)
-   [Tag: #dfs](https://brain.dennyzhang.com/tag/dfs)

---

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.  

The graph is given as follows:  the nodes are 0, 1, &#x2026;, graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.  

Example:  

    Input: [[1,2], [3], [3], []] 
    Output: [[0,1,3],[0,2,3]] 
    Explanation: The graph looks like this:
    0--->1
    |    |
    v    v
    2--->3
    There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Note:  

-   The number of nodes in the graph will be in the range [2, 15].
-   You can print different paths in any order, but you should keep the order of nodes inside one path.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/all-paths-from-source-to-target)  

Credits To: [leetcode.com](https://leetcode.com/problems/all-paths-from-source-to-target/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/all-paths-from-source-to-target