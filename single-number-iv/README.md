# LintCode: Single Number IV     :BLOG:Medium:


---

Single Number IV  

---

Similar Problems:  
-   [Single Number](https://brain.dennyzhang.com/single-number)
-   [Single Number II](https://brain.dennyzhang.com/single-number-ii)
-   [Single Number III](https://brain.dennyzhang.com/single-number-iii)
-   [Review: Binary Search Problems](https://brain.dennyzhang.com/review-binarysearch)
-   Tag: [#binarysearch](https://brain.dennyzhang.com/tag/binarysearch)

---

Give an array, all the numbers appear twice except one number which appears once and all the numbers which appear twice are next to each other. Find the number which appears once.  

Notice  
-   1 <= nums.length < 10^4
-   In order to limit the time complexity of the program, your program will run 10^5 times.

Example  

    Given nums = [3,3,2,2,4,5,5], return 4.
    
    Explanation:
    
    4 appears only once.

    Given nums = [2,1,1,3,3], return 2.
    
    Explanation:
    2 appears only once.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/single-number-iv)  

Credits To: [LintCode.com](http://www.lintcode.com/en/problem/single-number-iv/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/single-number-iv
    class Solution:
        """
        @param nums: The number array
        @return: Return the single number
        """
        def getSingleNumber(self, nums):
            ## Basic Ideas: binary search
            ## Complexity: Time O(log(n)), Space O(1)
            length = len(nums)
            if length == 1: return nums[0]
            # two corner cases
            if nums[0] != nums[1]: return nums[0]
            if nums[-1] != nums[-2]: return nums[-1]
    
            left, right = 0, length-1
            while left < right:
                mid = left + (right-left)/2
                if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                    return nums[mid]
    
                # same with left
                if nums[mid] == nums[mid-1]:
                    if (mid-1) % 2 == 0:
                        # right half
                        left = mid + 1
                    else:
                        right = mid - 2
                else:
                    if mid % 2 == 0:
                        # right half
                        left = mid + 2
                    else:
                        right = mid - 1
    
            # left equals right
            return nums[left]