# Leetcode: Graph Valid Tree     :BLOG:Basic:


---

Graph Valid Tree  

---

Similar Problems:  
-   Tag: [#bfs](https://code.dennyzhang.com/tag/bfs), [#classic](https://code.dennyzhang.com/tag/classic), [#hashmap](https://code.dennyzhang.com/tag/hashmap)

---

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.  

Example 1:  

    Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
    Output: true

Example 2:  

    Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    Output: false

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/graph-valid-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/graph-valid-tree/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

**General Thinkings:**  

In essence, how to check whether a graph has loop?  

    // Blog link: https://code.dennyzhang.com/graph-valid-tree
    // Basic Ideas: hashmap + bfs
    //
    // How a graph can be a tree:
    //  1. edge_count = node_count - 1
    //  2. No loop: any node can be the root
    //
    // How to check whether graph has loop?
    //
    // Complexity: Time O(v), Space O(v)
    //             v is edge count
    type Item struct {
      node, prev int
    }
    
    func validTree(n int, edges [][]int) bool {
        if len(edges) != n-1 { return false }
        // only one node
        if n==1 { return true }
        edges_map := map[int][]int{}
        for _, edge := range edges {
            i, j := edge[0], edge[1]
            edges_map[i] = append(edges_map[i], j)
            edges_map[j] = append(edges_map[j], i)
        }
        // any node can be the root, thus we choose the first one
        node := edges[0][0]
        // bfs
        queue := []Item{}
        queue = append(queue, Item{node, -1})
        visited := make([]bool, n)
        visited[node] = true
        for len(queue) != 0 {
            items := []Item{}
            for _, item := range queue {
                for _, node2 := range edges_map[item.node] {
                    if node2 == item.prev { continue }
                    if visited[node2] == true { return false }
                    items = append(items, Item{node2, item.node})
                    visited[node2] = true
                }
            }
            queue = []Item{}
            for _, item := range items {
                queue = append(queue, item)
            }
        }
        return true
    }