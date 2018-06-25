
# Leetcode: Ugly Number II     :BLOG:Medium:

---

Ugly Number II  

---

Similar Problems:  

-   [Leetcode: Ugly Number](https://code.dennyzhang.com/ugly-number)
-   Tag: [#mergesort](https://code.dennyzhang.com/tag/mergesort)

---

Write a program to find the n-th ugly number.  

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.  

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/ugly-number-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/ugly-number-ii/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/ugly-number-ii
    // Basic Ideas: BFS
    //
    //   Queue start with [1, 2, 3, 5]
    //   Find neighbors: multiple by [2, 3, 5]
    //   When to stop exploring?
    //
    // Complexity: Time O(1), Time O(1)
    func nthUglyNumber(n int) int {
        queue := []int{1, 2, 3, 5}
        s := map[int]bool{1: true, 2: true, 3:true, 5:true}
        l := []int{1, 2, 3, 5}
        for len(queue) != 0 {
    	// visit current layer
    	queue_count := len(queue)
    	for i := 0; i < queue_count; i++ {
    	    node := queue[0]
    	    // TODO: better performance
    	    queue = queue[1:]
    	    // get the next level
    	    for _, v := range []int{2, 3, 5} {
    		_, ok := s[node*v]
    		if ok == false {
    		    s[node*v] = true
    		    queue = append(queue, node*v)
    		    l = append(l, node*v)
    		}
    	    }
    	}
    	sort.Ints(queue)
        }
        sort.Ints(l)
        return l[n-1]
    }

