# Leetcode: Happy Number     :BLOG:Hard:


---

Happy Number  

---

Write an algorithm to determine if a number is "happy".  

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.  

    Example: 19 is a happy number
    
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/happy-number)  

Credits To: [Leetcode.com](https://leetcode.com/problems/happy-number/description/)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: Floyd Cycle
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def isHappy(self, n):
            """
            :type n: int
            :rtype: bool
            """
            slow = self.getCaculatedSum(n)
            fast = self.getCaculatedSum(self.getCaculatedSum(n))
            while slow != fast:
                slow = self.getCaculatedSum(slow)
                fast = self.getCaculatedSum(self.getCaculatedSum(fast))
            return True if slow == 1 else False
    
        def getCaculatedSum(self, n):
            if n < 0:
                return None
            if n == 0:
                return 0
            res = 0
            while n != 0:
                ldigit = n % 10
                res = res + ldigit*ldigit
                n = n/10
            return res