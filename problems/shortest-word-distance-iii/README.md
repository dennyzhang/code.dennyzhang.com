
# Leetcode: Shortest Word Distance III     :BLOG:Medium:

---

Shortest Word Distance III  

---

Similar Problems:  

-   [Shortest Word Distance](https://code.dennyzhang.com/shortest-word-distance)
-   [Shortest Word Distance II](https://code.dennyzhang.com/shortest-word-distance-ii)
-   Tag: [#array](https://code.dennyzhang.com/tag/array)

---

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.  

word1 and word2 may be the same and they represent two individual words in the list.  

Example:  

    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
    
    Input: word1 = "makes", word2 = "coding"
    Output: 1
    Input: word1 = "makes", word2 = "makes"
    Output: 3

Note:  
You may assume word1 and word2 are both in the list.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/shortest-word-distance-iii)  

Credits To: [leetcode.com](https://leetcode.com/problems/shortest-word-distance-iii/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/shortest-word-distance-iii
    // Basic Ideas: One pass
    // From left to right, get distance of word1 and word2
    //     Whenever we find a new word1 or word2, we update the corresponding index
    //     Note it's O(n), instead of O(n*n)
    //
    // Complexity: Time O(n), Space O(1)
    func shortestWordDistance(words []string, word1 string, word2 string) int {
        index1, index2 := -1, -1
        res := len(words)
        for i, word := range words {
    	if word1 == word2 && word == word1 {
    	    index1, index2 = index2, i
    	} else {
    	    if word == word1 { index1 = i }
    	    if word == word2 { index2 = i }
    	}
    	if index1 != -1 && index2 != -1 {
    	    distance := index1-index2
    	    if distance < 0 { distance = -distance }
    	    if distance<res { res = distance }
    	}
        }
        return res
    }

