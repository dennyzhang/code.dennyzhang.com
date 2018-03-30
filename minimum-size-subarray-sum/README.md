# Leetcode: Minimum Size Subarray Sum     :BLOG:Medium:


---

Minimum Size Subarray Sum  

---

Similar Problems:  
-   [Subarray Product Less Than K](https://brain.dennyzhang.com/subarray-product-less-than-k)
-   [Two Sum](https://brain.dennyzhang.com/two-sum)
-   [Review: TwoPointers Problems](https://brain.dennyzhang.com/review-twopointer)
-   [Review: Problems With Many Details](https://brain.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://brain.dennyzhang.com/tag/manydetails), [#twopointer](https://brain.dennyzhang.comy/tag/twopointer)

---

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum >= s. If there isn't one, return 0 instead.  

For example, given the array [2,3,1,2,4,3] and s = 7,  
the subarray [4,3] has the minimal length under the problem constraint.  

More practice:  
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/minimum-size-subarray-sum)  

Credits To: [leetcode.com](https://leetcode.com/problems/minimum-size-subarray-sum/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/minimum-size-subarray-sum
    ## Basic Ideas: Two pointers + Ge accumulated sum
    ##
    ##   Corner case: 0 elements or 1 elements
    ##   Right pointer move one step each time.
    ##   Left pointer don't need to move left. Why? We only need to find the minimal length
    ##
    ## Complexity: Time O(n), Space O(1)
    import sys
    class Solution:
        def minSubArrayLen(self, s, nums):
            """
            :type s: int
            :type nums: List[int]
            :rtype: int
            """
            length = len(nums)
            if length == 0: return 0
    
            min_length = sys.maxsize
            left, sum_v = 0, 0
    
            # always move right by 1 step
            for right in range(0, length):
                sum_v += nums[right]
                while sum_v >=s:
                    min_length = min(min_length, right-left+1)
                    # left won't pass right. Why? Because s>0
                    sum_v -= nums[left]
                    left += 1
    
            return min_length if min_length != sys.maxsize else 0