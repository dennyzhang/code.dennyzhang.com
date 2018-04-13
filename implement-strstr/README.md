# Leetcode: Implement strStr()     :BLOG:Basic:


---

Implement strStr()  

---

Similar Problems:  
-   [Review: String Problems](https://code.dennyzhang.com/review-string), Tag: [#string](https://code.dennyzhang.com/tag/string)

---

Implement strStr().  

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.  

Example 1:  

    Input: haystack = "hello", needle = "ll"
    Output: 2

Example 2:  

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/implement-strstr)  

Credits To: [leetcode.com](https://leetcode.com/problems/implement-strstr/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/implement-strstr
    ## Idea:
    ## Complexity: Time O(n*k), Space O(1)
    ##    hello, hello
    ##       lo
    class Solution(object):
        def strStr(self, haystack, needle):
            """
            :type haystack: str
            :type needle: str
            :rtype: int
            """
            h_length = len(haystack)
            n_length = len(needle)
            if n_length == 0:
                return 0
    
            for i in range(0, h_length-n_length+1):
                if haystack[i:(i+n_length)] == needle:
                    return i
            return -1