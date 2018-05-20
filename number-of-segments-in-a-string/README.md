# Leetcode: Number of Segments in a String     :BLOG:Basic:


---

Segement string  

---

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.  

Please note that the string does not contain any non-printable characters.  

    Example:
    
    Input: "Hello, my name is John"
    Output: 5

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/number-of-segments-in-a-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/number-of-segments-in-a-string/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/number-of-segments-in-a-string
    ## Basic Ideas: one pass. 2 pointer
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def countSegments(self, s):
            """
            :type s: str
            :rtype: int
            """
            res = 0
            i = 0
            while True:
                while i<len(s) and s[i] == ' ':
                    i += 1
    
                if i>=len(s):
                    break
                res += 1
                while i<len(s) and s[i] != ' ':
                    i += 1
            return res