# LintCode: Reverse Array     :BLOG:Basic:


---

Reverse Array  

---

Similar Problems:  
-   [Review: TwoPointers Problems](https://brain.dennyzhang.com/review-twopointer), [Tag: #twopointer](https://brain.dennyzhang.com/tag/twopointer)

---

Reverse the given array nums inplace.  

 Notice  
Inplace means you can't use extra space.  

Example  

    Given nums = [1,2,5]
    return [5,2,1]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reverse-array)  

Credits To: [LintCode.com](http://www.lintcode.com/en/problem/reverse-array/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/reverse-array
    class Solution:
        """
        @param nums: a integer array
        @return: nothing
        """
        def reverseArray(self, nums):
            ## Basic Ideas: two pointer
            ## Complexity: Time O(n), Space O(1)
            l, r = 0, len(nums)-1
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1