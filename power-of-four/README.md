# Leetcode: Power of Four     :BLOG:Medium:


---

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.  

---

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.  

Example:  
Given num = 16, return true. Given num = 5, return false.  

Follow up: Could you solve it without loops/recursion?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/power-of-four)  

Credits To: [leetcode.com](https://leetcode.com/problems/power-of-four/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def isPowerOfFour(self, num):
            return ((num - 1) & num == 0 and (num-1) % 3 == 0)