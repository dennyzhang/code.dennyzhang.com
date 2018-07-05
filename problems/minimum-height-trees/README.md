
# Leetcode: Minimum Height Trees     :BLOG:Medium:

---

Minimum Height Trees  

---

Similar Problems:  

-   [Trapping Rain Water II](https://code.dennyzhang.com/trapping-rain-water-ii)
-   Tag: [#bfs](https://code.dennyzhang.com/category/bfs), [#inspiring](https://code.dennyzhang.com/category/inspiring), [#outer2inside](https://code.dennyzhang.com/tag/outer2inside)

---

For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.  

Format  
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).  

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.  

Example 1:  

    Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]
    
            0
            |
            1
           / \
          2   3
    return [1]

Example 2:  

    Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    
         0  1  2
          \ | /
            3
            |
            4
            |
            5
    return [3, 4]

Note:  

1.  According to the definition of tree on Wikipedia: "a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree."
2.  The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/minimum-height-trees)  

Credits To: [leetcode.com](https://leetcode.com/problems/minimum-height-trees/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/minimum-height-trees
    // Basic Ideas:
    // There are at most 2 MHTs
    // We keep removing leaf nodes. The remaining one or two nodes are targets
    // Complexity: Time O(n), Space O(n)
    func findMinHeightTrees(n int, edges [][]int) []int {
        if n == 1 { return []int{0} }
        relations := make([]map[int]bool, n)
        for i:= 0; i<n; i++ { relations[i] = map[int]bool{}}
        for _, edge := range edges {
    	p, q := edge[0], edge[1]
    	relations[p][q], relations[q][p] = true, true
        }
        queue := []int{}
        // start with leaf nodes
        for i:=0; i<n; i++ {
    	if len(relations[i]) == 1 { queue = append(queue, i) }
        }
    
        for n>2 {
    	// explore current level
    	n -= len(queue)
    	items := []int{}
    	for _, node := range queue {
    	    for node2 := range relations[node] {
    		delete (relations[node2], node)
    		// inner layer
    		if len(relations[node2]) == 1 { items = append(items, node2) }
    	    }
    	}
    	queue = items
        }
        return queue
    }

