# Leetcode: Ugly Number     :BLOG:Medium:


---

Check whether a given number is an ugly number.  

---

Write a program to check whether a given number is an ugly number.  

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.  

Note that 1 is typically treated as an ugly number.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/ugly-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/ugly-number/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/ugly-number
    class Solution(object):
        def isUgly(self, num):
            """
            :type num: int
            :rtype: bool
            """
            if num <= 0:
                return False
    
            for power in [2, 3, 5]:
                while num % power == 0 and num != 0:
                    num = num / power
    
            return num == 1