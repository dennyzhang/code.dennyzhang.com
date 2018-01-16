# Leetcode: Pow(x, n)     :BLOG:Basic:


---

Implement pow(x, n).  

---

Implement pow(x, n).  

    Example 1:
    
    Input: 2.00000, 10
    Output: 1024.00000

    Example 2:
    
    Input: 2.10000, 3
    Output: 9.26100

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/powx-n)  

Credits To: [Leetcode.com](https://leetcode.com/problems/powx-n/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def myPow(self, x, n):
            """
            :type x: float
            :type n: int
            :rtype: float
            """
            ## Idea: x^n = x^(n/2) * x^(n/2) * x^(n%2)
            ## Complexity: Time O(log(n)), Space O(1)
            ## Sample Data:
            ##   pow(5, 3) = 5*5*5
            ##   pow(5, -3) = ?
            ##   pow(-5, 3) = (-5)*(-5)*(-5)
            ##   pow(5.1, 3) = 5.1*5.1*5.1
            ##   x^n = x^(n/2) * x^(n/2) * x^(n%2)
            ##   pow(x, -n) = 1/pow(x, n)
            if n == 0:
                return 1
            if n < 0:
                return 1/self.myPow(x, -n)
            if n == 1:
                return x
            if(n>=2):
                val = self.myPow(x, n/2)
                return val*val*self.myPow(x, n%2)