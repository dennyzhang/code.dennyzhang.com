# Leetcode: Reverse Integer     :BLOG:Basic:


---

Reverse Integer  

---

Given a 32-bit signed integer, reverse digits of an integer.  

Example 1:  

Input: 123  
Output:  321  
Example 2:  

Input: -123  
Output: -321  
Example 3:  

Input: 120  
Output: 21  
Note:  
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reverse-integer)  

Credits To: [leetcode.com](https://leetcode.com/problems/reverse-integer/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/reverse-integer
    class Solution(object):
        def reverse(self, x):
            """
            :type x: int
            :rtype: int
            """
            if(abs(x) > (2 ** 31 - 1)):
                return 0
            y = 0
            if x == 0:
                return x
    
            is_negative = (x<0)
    
            if is_negative is True:
                x = -x
    
            while x != 0:
                y = y*10 + (x % 10)
                x = x/10
    
            if(abs(y) > (2 ** 31 - 1)):
                return 0
    
            if is_negative is True:
                return -y
            else:
                return y
    
    if __name__ == '__main__':
        s = Solution()
        print s.reverse(0)
        print s.reverse(123)
        print s.reverse(-123)