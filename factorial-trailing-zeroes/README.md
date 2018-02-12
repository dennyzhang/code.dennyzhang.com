# Leetcode: Factorial Trailing Zeroes     :BLOG:Amusing:


---

Factorial Trailing Zeroes  

---

Given an integer n, return the number of trailing zeroes in n!.  

Note: Your solution should be in logarithmic time complexity.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/factorial-trailing-zeroes)  

Credits To: [leetcode.com](https://leetcode.com/problems/factorial-trailing-zeroes/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/factorial-trailing-zeroes
    class Solution(object):
        def trailingZeroes(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n < 0: return None
            if n == 0 or n == 1: return 0
    
            import math
            k = int(math.log(n, 5))
            # print "k: %d" % (k)
            res = 0
            pow_val = 5
            for i in xrange(1, k+1):
                res += n/pow_val
                pow_val *= 5
            return res