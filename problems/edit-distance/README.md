
# Leetcode: Edit Distance     :BLOG:Hard:

---

Edit Distance  

---

Similar Problems:  

-   [Delete Operation for Two Strings](https://code.dennyzhang.com/delete-operation-for-two-strings)
-   [Unique Paths](https://code.dennyzhang.com/unique-paths)
-   [One Edit Distance](https://code.dennyzhang.com/one-edit-distance)
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming), [#dp2order](https://code.dennyzhang.com/tag/dp2order), [#classic](https://code.dennyzhang.com/tag/classic), [#redo](https://code.dennyzhang.com/tag/redo), [#padplaceholder](https://code.dennyzhang.com/tag/padplaceholder)

---

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)  

You have the following 3 operations permitted on a word:  

a) Insert a character  
b) Delete a character  
c) Replace a character  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/edit-distance)  

Credits To: [leetcode.com](https://leetcode.com/problems/edit-distance/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: dp - Time O(n\*m), Space O(n\*m)

    // Blog link: https://code.dennyzhang.com/edit-distance
    // Basic Ideas: dp second order
    //
    // dp[i][j]: match word1 0:i with word2 0:j
    // Then how we get dp[i][j] from previous caculation?
    //     If word1[i] == word[j], dp[i-1][j-1]
    //     Otherwise, we can make 3 choices
    //       - Replace word1[i], dp[i-1][j-1]+1
    //       - Delete word1[i-1], dp[i-1][j]+1
    //       - Add word[j] to word1, dp[i][j-1]+1
    // Complexity: Time O(n*m), Space O(n*m)
    func minDistance(word1 string, word2 string) int {
        len1, len2 := len(word1), len(word2)
        if len1 == 0 || len2 == 0 { return len1+len2 }
        dp := make([][]int, len1)
        for i := range dp { dp[i] = make([]int, len2) }
        // Initialize
        if word1[0]!=word2[0] { dp[0][0] = 1 }
        for j:=1; j<len2; j++ {
    	dp[0][j] = dp[0][j-1]+1
    	if word2[j] == word1[0] && dp[0][j] == j+1 {
    	    dp[0][j] = j
    	}
        }
        for i:=1; i<len1; i++ {
    	dp[i][0] = dp[i-1][0]+1
    	if word1[i] == word2[0] && dp[i][0] == i+1 {
    	    dp[i][0] = i
    	}
        }
        // dp
        for i:=1; i<len1; i++ {
    	for j:=1; j<len2; j++ {
    	    if word1[i] == word2[j] {
    		dp[i][j] = dp[i-1][j-1]
    		continue
    	    }
    	    min := dp[i-1][j-1]+1
    	    if dp[i-1][j]+1 < min { min = dp[i-1][j]+1 }
    	    if dp[i][j-1]+1 < min { min = dp[i][j-1]+1 }
    	    dp[i][j] = min
    	}
        }
        return dp[len1-1][len2-1]
    }

-   Solution: dp - Time O(n\*m), Space O(n)

    // Blog link: https://code.dennyzhang.com/edit-distance
    // Basic Ideas: dp second order
    //
    // Two major improvements compared to intuitive dp[][]
    // 1. We add a dummy " " to the head. Thus the logic of base cases can be dramatically simplified
    // 2. Reduce space complexity from O(n*m) to O(n)
    // Complexity: Time O(n*m), Space O(n)
    func minDistance(word1 string, word2 string) int {
        len1, len2 := len(word1), len(word2)
        if len1 == 0 || len2 == 0 { return len1+len2 }
        dp := make([]int, len2+1)
        // initialize
        for i:=0; i<=len2; i++ { dp[i] = i }
        // dp
        for i:=1; i<=len1; i++ {
    	prev := i-1
    	dp[0] = i
    	for j:=1; j<=len2; j++ {
    	    cur := -1
    	    if word1[i-1] == word2[j-1] {
    		cur = prev
    	    } else {
    		// replace
    		cur = dp[j-1]+1
    		// delete
    		if prev+1 < cur { cur = prev+1 }
    		// add
    		if dp[j]+1 < cur { cur = dp[j]+1 }
    	    }
    	    prev = dp[j]
    	    dp[j] = cur
    	}
        }
        return dp[len2]
    }

