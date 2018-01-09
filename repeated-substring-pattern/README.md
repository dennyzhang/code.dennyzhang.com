# Puzzle: Repeated Substring Pattern     :BLOG:Numbers:


---

Check whether string can be created by keep repeating one substring.  

---

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.  

Example 1:  

    Input: "abab"
    
    Output: True

Explanation: It's the substring "ab" twice.  
Example 2:  

    Input: "aba"
    
    Output: False

Example 3:  

    Input: "abcabcabcabc"
    
    Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)  

Credits To: [Leetcode.com](https://leetcode.com/problems/repeated-substring-pattern/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def repeatedSubstringPattern(self, s):
            """
            :type s: str
            :rtype: bool
            """

More Reading:  
-   [Puzzle: Find the Duplicate Number](http://brain.dennyzhang.com/find-duplicate-num/)