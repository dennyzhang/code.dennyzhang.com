# Leetcode: Power of Two     :BLOG:Medium:


---

Given an integer, write a function to determine if it is a power of two.  

---

Given an integer, write a function to determine if it is a power of two.  

Blog link: <http://brain.dennyzhang.com/power-of-two>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/power-of-two)  

Credits To: [leetcode.com](https://leetcode.com/problems/power-of-two/description)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def isPowerOfTwo(self, n):
            """
            :type n: int
            :rtype: bool
            """
            if n <= 0:
                return False
            return n & (n-1) == 0