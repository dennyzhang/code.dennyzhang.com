# Leetcode: 3Sum     :BLOG:Medium:


---

3Sum  

---

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.  

Note: The solution set must not contain duplicate triplets.  

    For example, given array S = [-1, 0, 1, 2, -1, -4],
    
    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/3sum)  

Credits To: [leetcode.com](https://leetcode.com/problems/3sum/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/3sum
    ## Basic Ideas: sort the list, then loop with idea of 2 sum
    ##       What if you have duplicate entries?
    ##       [0, 0, 0, 0]
    ## Complexity: Time O(n*n), Space O(1)
    ## Sample Data:
    ##      -4 -1 -1 0 1 2
    ##       i l         r
    class Solution(object):
        def threeSum(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            ret = []
            nums.sort()
    
            for i in xrange(len(nums)-2):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                l,r = i+1, len(nums)-1
                while l<r:
                    val = nums[i] + nums[l] + nums[r]
                    if val >0:
                        r -= 1
                    elif val < 0:
                        l += 1
                    else:
                        ret.append([nums[i], nums[l], nums[r]])
                        while l<r and nums[l] == nums[l+1]:
                            l += 1
                        while l<r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1; r -=1
            return ret