# Leetcode: Is Subsequence     :BLOG:Basic:


---

Is Subsequence  

---

Similar Problems:  
-   Tag: [#basic](https://code.dennyzhang.com/category/basic)

---

Given a string s and a string t, check if s is subsequence of t.  

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).  

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).  

Example 1:  

    s = "abc", t = "ahbgdc"
    
    Return true.

Example 2:  

    s = "axc", t = "ahbgdc"
    
    Return false.

Follow up:  
If there are lots of incoming S, say S1, S2, &#x2026; , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/is-subsequence)  

Credits To: [leetcode.com](https://leetcode.com/problems/is-subsequence/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/is-subsequence
    ## Basic Ideas: Greedy + Two pointer
    ##
    ## Complexity: Time O(1), Space O(1).
    class Solution:
        def isSubsequence(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            length = len(s)
            if length == 0: return True
            index = 0
            for i in range(0, len(t)):
                if t[i] == s[index]: index += 1
                if index == length: return True
            return False