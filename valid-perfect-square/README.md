# Leetcode: Valid Perfect Square     :BLOG:Amusing:


---

Valid Perfect Square  

---

Given a positive integer num, write a function which returns True if num is a perfect square else False.  

Note: Do not use any built-in library function such as sqrt.  

    Example 1:
    
    Input: 16
    Returns: True

    Example 2:
    
    Input: 14
    Returns: False

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/valid-perfect-square)  

Credits To: [leetcode.com](https://leetcode.com/problems/valid-perfect-square/description/)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: Binary search
    ##             Search in between [1^2, 2^2, 3^2, ... num^2]
    ## Complexity: Time O(log(n)), Space O(1)
    class Solution(object):
        def isPerfectSquare(self, num):
            """
            :type num: int
            :rtype: bool
            """
            if num <= 0:
                return False
            left, right = 1, num
            while left<= right:
                mid = left + (right-left)/2
                v = mid*mid
                if v == num:
                    return True
                elif v < num:
                    left = mid + 1
                else:
                    right = mid - 1
            return False