# Leetcode: Single Number     :BLOG:Easy:


---

Identity number which appears exactly once.  

---

Given an array of integers, every element appears twice except for one. Find that single one.  

Note:  
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/single-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/single-number/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/single-number
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