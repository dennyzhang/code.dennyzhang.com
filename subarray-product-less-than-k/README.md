# Leetcode: Subarray Product Less Than K     :BLOG:Medium:


---

Subarray Product Less Than K  

---

Similar Problems:  
-   [Minimum Size Subarray Sum](https://code.dennyzhang.com/minimum-size-subarray-sum)
-   [Subarray Sum Equals K](https://code.dennyzhang.com/subarray-sum-equals-k)
-   [Review: TwoPointers Problems](https://code.dennyzhang.com/review-twopointer), [Tag: #twopointer](https://code.dennyzhang.com/tag/twopointer)

---

Your are given an array of positive integers nums.  

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.  

Example 1:  

    Input: nums = [10, 5, 2, 6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:  

-   0 < nums.length <= 50000.
-   0 < nums[i] < 1000.
-   0 <= k < 10^6.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/subarray-product-less-than-k)  

Credits To: [leetcode.com](https://leetcode.com/problems/subarray-product-less-than-k/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/subarray-product-less-than-k
    ## Basic Ideas: two pointers
    ##     All nubmers are positive integers. 
    ##     So if we enlarge the window, the suarray product will increase.
    ##
    ##     right pointer move one step each time
    ##     If product of current window is less than k, get the count of possibilities.
    ##     Otherwise move the left
    ##
    ## Complexity:
    class Solution:
        def numSubarrayProductLessThanK(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            length = len(nums)
            if length == 0: return 0
            res = 0
            left, curProduct = 0, 1
            for right in range(0, length):
                curProduct *= nums[right]
                # keep moving the left, if it's too big
                while left <= right and curProduct >= k:
                    curProduct = int(curProduct/nums[left])
                    left += 1 
    
                # print(left, right, curProduct)
                if curProduct < k:
                    # get all the possilities with nums[right] chosen
                    res += right-left+1
            return res