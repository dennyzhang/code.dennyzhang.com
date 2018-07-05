
# Leetcode: Map Sum Pairs     :BLOG:Medium:

---

Map Sum Pairs  

---

Similar Problems:  

-   [Review: Trie Tree Problems](https://code.dennyzhang.com/review-trie)
-   Tag: [#trie](https://code.dennyzhang.com/tag/trie)

---

Implement a MapSum class with insert, and sum methods.  

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.  

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.  

Example 1:  

    Input: insert("apple", 3), Output: Null
    Input: sum("ap"), Output: 3
    Input: insert("app", 2), Output: Null
    Input: sum("ap"), Output: 5

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/map-sum-pairs)  

Credits To: [leetcode.com](https://leetcode.com/problems/map-sum-pairs/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/map-sum-pairs
    // Basic Ideas: Trie Tree
    // Complexity: Time ?, Space ?
    
    type MapSum struct {
        children map[string]*MapSum
        val int
        isLeaf bool
    }
    
    /** Initialize your data structure here. */
    func Constructor() MapSum {
        root := MapSum{make(map[string]*MapSum), 0, false}
        return root
    }
    
    func (this *MapSum) Insert(key string, val int)  {
        node := this
        for i := 0; i < len(key); i++ {
    	ch := string(key[i])
    	p, ok := node.children[ch]
    	if ok == false {
    	    p = &MapSum{make(map[string]*MapSum), 0, false}
    	    node.children[ch] = p
    	}
    	node = p
        }
        node.isLeaf = true
        node.val = val
    }
    
    func (this *MapSum) Sum(prefix string) int {
        node := this
        // fmt.Print(node, "\n")
        i := 0;
        for ; i < len(prefix); i++ {
    	ch := string(prefix[i])
    	p, ok := node.children[ch]
    	if ok == true {
    	    node = p
    	} else {
    	    break
    	}
        }
    
        if i != len(prefix) {
    	// haven't found this prefix
    	return 0
        } else {
    	// sum all the leaf nodes
    	res := 0
    	queue := []*MapSum{node}
    	for len(queue) != 0 {
    	    queue_count := len(queue)
    	    for i:=0; i<queue_count; i++ {
    		node = queue[0]
    		// collect result of leaf
    		if node.isLeaf == true {
    		    res += node.val
    		}
    		queue = queue[1:]
    		// get the next level
    		for ch := range node.children {
    		    queue = append(queue, node.children[ch])
    		}
    	    }
    	}
    	return res
        }
    }
    
    /**
     * Your MapSum object will be instantiated and called as such:
     * obj := Constructor();
     * obj.Insert(key,val);
     * param_2 := obj.Sum(prefix);
     */

