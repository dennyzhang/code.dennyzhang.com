# LintCode: Longest Repeating Substring     :BLOG:Medium:


---

Longest Repeating Substring  

---

Similar Problems:  
-   Tag: [#string](https://code.dennyzhang.com/tag/string)

---

Given a string str, find the longest substring with no fewer than k repetitions and return the length. The substring can have overlapping parts, but cannot completely overlap.  

Notice  
-   1 <= str.length <= 1000
-   1 < k < str.length
-   We guarantee that the problem will certainly can be solved

Example  

    Given str = "aaa", k = 2, return 2.
    
    Explanation:
    The longest subsequence with no fewer than k repetitions is "aa", and the length is 2.

    Given str = "aabcbcbcbc", k = 2, return 6.
    
    Explanation:
    Subsequences repeat no fewer than twice are "a", "bc", "bcbc" and "bcbcbc", and the longest is "bcbcbc", and the length is 6.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/longest-repeating-substring)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/longest-repeating-substring/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/longest-repeating-substring
    class Solution:
        """
        @param str: The input string
        @param k: The repeated times
        @return: The answer
        """
        def longestRepeatingSubsequenceII(self, str, k):