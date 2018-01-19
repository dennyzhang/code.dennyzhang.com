# Leetcode: Repeated Substring Pattern     :BLOG:Hard:


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

Blog link: <http://brain.dennyzhang.com/repeated-substring-pattern>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def repeatedSubstringPattern(self, s):
            """
            :type s: str
            :rtype: bool
            """

More Reading:  
-   [[<http://brain.dennyzhang.com/repeated-substring-pattern>