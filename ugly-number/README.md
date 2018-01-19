# Leetcode: Ugly Number     :BLOG:Medium:


---

Check whether a given number is an ugly number.  

---

Write a program to check whether a given number is an ugly number.  

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.  

Note that 1 is typically treated as an ugly number.  

Blog link: <http://brain.dennyzhang.com/ugly-number>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

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