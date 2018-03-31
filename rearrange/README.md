# LintCode: Rearrange     :BLOG:Basic:


---

Rearrange  

---

Similar Problems:  
-   [Wiggle Sort](https://brain.dennyzhang.com/wiggle-sort)

---

Given an array required to be rearranged, which means all the numbers on the even-numbered bits are less than those on the odd-numbered bits. At the same time, the even-numbered bits are sorted in ascending order, and the odd-numbered bits are also sorted in ascending order.  

Notice  
-   The length of the array is n, n <= 100000
-   The index of the array is started from 0
-   Have you met this question in a real interview?

Example  
Given array = [-1,0,1,-1,5,10], return [-1,1,-1,5,0,10].  

    Explanation:
    [-1,1,-1,5,0,10] meets the requirements.

Given array = [2,0,1,-1,5,10], return [-1,2,0,5,1,10].  

    Explanation:
    [-1,2,0,5,1,10] meets the requirements.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/rearrange)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/rearrange/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/rearrange
    class Solution:
        """
        @param nums: the num arrays 
        @return: the num arrays after rearranging
        """
        def rearrange(self, nums):
            # Write your code here 
            ## Basic Ideas: Sort
            ## Assumption: we can always have one solution
            ## Complexity: Time O(n*log(n)), Space O(n)
            nums.sort()
            length = len(nums)
    
            res = []
            if length%2 == 0:
                k = int(length/2)
            else:
                k = int(length/2)+1
    
            for i in range(int(length/2)):
                res.append(nums[i])
                res.append(nums[i+k])
    
            if length%2 != 0:
                res.append(nums[int(length/2)])
            return res