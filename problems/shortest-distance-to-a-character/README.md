
# Leetcode: Shortest Distance to a Character     :BLOG:Basic:

---

Shortest Distance to a Character  

---

Similar Problems:  

-   [Product of Array Except Self](https://code.dennyzhang.com/product-of-array-except-self)
-   [Review: BFS Problems](https://code.dennyzhang.com/review-bfs)
-   Tag: [#bfs](https://code.dennyzhang.com/tag/bfs), [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#twopass](https://code.dennyzhang.com/tag/twopass)

---

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.  

Example 1:  

    Input: S = "loveleetcode", C = 'e'
    Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Note:  

-   S string length is in [1, 10000].
-   C is a single character, and guaranteed to be in string S.
-   All letters in S and C are lowercase.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/shortest-distance-to-a-character)  

Credits To: [leetcode.com](https://leetcode.com/problems/shortest-distance-to-a-character/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution 1: BFS

    // Blog link: https://code.dennyzhang.com/shortest-distance-to-a-character
    // Basic Ideas: BFS
    // Complexity: Time O(n), Space O(1)
    func shortestToChar(S string, C byte) []int {
        res := make([]int, len(S))
        queue := []int{}
        for i, ch := range S {
    	if byte(ch) == C {
    	    queue = append(queue, i)
    	    res[i] = 0
    	} else {
    	    res[i] = -1
    	}        
        }
        level := 0
        // BFS
        for len(queue) != 0 {
    	level += 1
    	len_queue := len(queue)
    	for i:=0; i<len_queue; i++ {
    	    index := queue[0]
    	    queue = queue[1:]
    	    for _, offset := range []int{1, -1} {
    		index2 := index+offset
    		if index2>=0 && index2<=len(S)-1 && res[index2] == -1 {
    		    queue = append(queue, index2)
    		    res[index2] = level
    		}
    	    }
    	}
        }
        return res
    }

-   Solution 2: Two pass. Update + Adjustment

    // Blog link: https://code.dennyzhang.com/shortest-distance-to-a-character
    // Basic Ideas: Two pass
    //    Pass 1: left to right. Distance from previous C
    //    Pass 2: right to left. Distance for min(old_distance, distance_from_following_C)
    // Complexity: Time O(n), Space O(1)
    func shortestToChar(S string, C byte) []int {
        res := make([]int, len(S))
        index := -len(S)
        for i, ch := range S {
    	if ch == rune(C) { index = i }
    	res[i] = i-index
        }
    
        index = 2*len(S)
        for i := len(S)-1; i>=0; i-- {
    	ch := S[i]
    	if ch == C { index = i}
    	if index-i < res[i] { res[i] = index-i }
        }
        return res
    }

