# Lintcode: Digital Flip     :BLOG:Medium:


---

Digital Flip  

---

Similar Problems:  
-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming), [Tag: #dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

Give you an array of 01. Find the minimum number of flipping steps so that the array meets the following rules:  
The back of 1 can be either1 or 0, but0 must be followed by 0.  

Notice  
-   The length of the given array n <= 100000.

Example  

    Given array = [1,0,0,1,1,1], return 2.
    
    Explanation:
    Turn two 0s into 1s.

    Given array = [1,0,1,0,1,0], return 2.
    
    Explanation:
    Turn the second 1 and the third 1 into 0.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/digital-flip)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/digital-flip/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/digital-flip
    class Solution:
        """
        @param nums: the array
        @return: the minimum times to flip digit
        """
        def flipDigit(self, nums):
            ## Basic Ideas: dynamic programming
            ## Complexity: Time O(n), Space O(1)
            length = len(nums)
            if length <= 1: return 0
            if nums[0] == 0:
                min1, min2 = 0, 1
            else:
                min1, min2 = 1, 0
            for i in range(1, length):
                if nums[i] == 0:
                    min1, min2 = min(min1, min2), 1+min2
                else:
                    min1, min2 = 1+min(min1, min2), min2
            return min(min1, min2)