# Leetcode: Single Number     :BLOG:Easy:


---

Identity number which appears exactly once.  

---

Given an array of integers, every element appears twice except for one. Find that single one.  

Note:  
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?  

Blog link: <http://brain.dennyzhang.com/single-number>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

    class Solution(object):
        def singleNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            x = 0
            for i in nums:
                x = x ^ i
            return x
    
    if __name__ == '__main__':
        s = Solution()
        print s.singleNumber([1, 2, 1])
        print s.singleNumber([2, 2, 1])

Leave me comments, if you know how to solve.  

More Reading:  
-   [[<http://brain.dennyzhang.com/single-number>
-   [[<http://brain.dennyzhang.com/single-number>
-   [[<http://brain.dennyzhang.com/single-number>