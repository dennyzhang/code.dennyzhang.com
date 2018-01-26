# Leetcode: Reverse String     :BLOG:Basic:


---

Reverse String  

---

Write a function that takes a string as input and returns the string reversed.  

Example:  
Given s = "hello", return "olleh".  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reverse-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/reverse-string/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/reverse-string
    class Solution(object):
        def reverseString(self, s):
            """
            :type s: str
            :rtype: str
            """
            return s[::-1]