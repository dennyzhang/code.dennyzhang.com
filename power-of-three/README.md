# Leetcode: Power of Three     :BLOG:Amusing:


---

Given an integer, write a function to determine if it is a power of three.  

---

Given an integer, write a function to determine if it is a power of three.  

Follow up:  
Could you do it without using any loop / recursion?  

Blog link: <http://brain.dennyzhang.com/power-of-three>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/power-of-three)  

Credits To: [leetcode.com](https://leetcode.com/problems/power-of-three/description)  

Leave me comments, if you know how to solve.  

    class Solution(object):
    ## Basic Ideas: power of any prime number
    ##              3 is a prime
    ##              If 3 % k == 0 and k is a prime, then k is 3.
    ##              Thus 3^19 % n === 0 means n is power of 3
    class Solution(object):
        def isPowerOfThree(self, n):
            """
            :type n: int
            :rtype: bool
            """
            if n <= 0:
                return False
            larget_power3 = pow(3, 19)
            return larget_power3 % n == 0