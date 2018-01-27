# Leetcode: Clone Graph     :BLOG:Basic:


---

Clone Graph  

---

Similar Problems:  
-   Tag: [#basic](http://brain.dennyzhang.com/tag/basic)

---

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.  

OJ's undirected graph serialization:  
Nodes are labeled uniquely.  

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.  
As an example, consider the serialized graph {0,1,2#1,2#2,2}.  

The graph has a total of three nodes, and therefore contains three parts as separated by #.  

1.  First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
2.  Second node is labeled as 1. Connect node 1 to node 2.
3.  Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
4.  Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/clone-graph)  

Credits To: [leetcode.com](https://leetcode.com/problems/clone-graph/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/clone-graph
    ## Basic Ideas: Use a hashmap
    ##              For each new node, create one.
    ##              Scan its neighbors, if found new nodes. Create them. And update mapping
    ##              Update children
    ##
    ## Complexity: Time O(n*n), Space O(n).
    ##
    # Definition for a undirected graph node
    # class UndirectedGraphNode:
    #     def __init__(self, x):
    #         self.label = x
    #         self.neighbors = 
    
    class Solution:
        # @param node, a undirected graph node
        # @return a undirected graph node
        def cloneGraph(self, node):
            if node is None: return None
            d = {}
            self.DFSClone(node, d)
            return d[node][0]
    
        def DFSClone(self, node, d):
            if node is None: return None
            if node not in d:
                newNode = UndirectedGraphNode(node.label)
                d[node] = (newNode, False)
            (newNode, has_finished) = d[node]
            if has_finished is True:
                return newNode
    
            # mark as DONE to avoid duplicate visits
            d[node] = (newNode, True)
            for neighbor in node.neighbors:
                newNeighbor = self.DFSClone(neighbor, d)
                newNode.neighbors.append(newNeighbor)
            return newNode