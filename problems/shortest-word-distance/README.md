
# Leetcode: Shortest Word Distance     :BLOG:Basic:

---

Shortest Word Distance  

---

Similar Problems:  

-   [Heaters](https://code.dennyzhang.com/heaters)
-   [Shortest Word Distance II](https://code.dennyzhang.com/shortest-word-distance-ii)
-   [Shortest Word Distance III](https://code.dennyzhang.com/shortest-word-distance-iii)
-   Tag: [#array](https://code.dennyzhang.com/tag/array), [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#classic](https://code.dennyzhang.com/tag/classic)

---

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.  

For example,  

    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
    
    Given word1 = "coding", word2 = "practice", return 3.
    Given word1 = "makes", word2 = "coding", return 1.

Note:  
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/shortest-word-distance)  

Credits To: [leetcode.com](https://leetcode.com/problems/shortest-word-distance/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/shortest-word-distance
    // Basic Ideas: One pass
    //
    // Mininum distance between two items in a list
    //
    // From left to right, get distance of word1 and word2
    //     Whenever we find a new word1 or word2, we update the corresponding index
    //     Note it's O(n), instead of O(n*n)
    //
    // Complexity: Time O(n), Space O(1)
    func shortestDistance(words []string, word1 string, word2 string) int {
        index1, index2 := -1, -1
        res := len(words)
        for i, word := range words {
    	if word == word1 { index1 = i }
    	if word == word2 { index2 = i }
    	if index1 != -1 && index2 != -1 {
    	    distance := index1-index2
    	    if distance < 0 { distance = -distance }
    	    if distance<res { res = distance }
    	}
        }
        return res
    }

