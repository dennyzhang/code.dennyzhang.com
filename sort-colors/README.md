# Puzzle: Sort Colors     :BLOG:Numbers:


---

Array is composed by only 3 types of elements. Sort it fast.  

---

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.  

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.  

Credits To: [Leetcode.com](https://leetcode.com/problems/sort-colors/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def sortColors(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            ## Idea: one pass. left, cur, right
            ##         left=0, right=len(nums)-1, cur = 0
            ##         1. nums[cur] is 1, cur++
            ##         2. nums[cur] is 0, swap with left, and left++, cur++
            ##         3. nums[cur] is 2, swap with right, and right--. cur doesn't change
            ##         When cur>right, break
            ## Complexity
            ## Sample Data:
            ##     0 1 2 0 1 2 0
            length = len(nums)
            if length <= 1:
                return
            left, right, cur = 0, length-1, 0
            while cur <= right:
                if nums[cur] == 1:
                    cur += 1
                elif nums[cur] == 0:
                    nums[left], nums[cur] = nums[cur], nums[left]
                    left, cur = left+1, cur+1
                else:
                    nums[right], nums[cur] = nums[cur], nums[right]
                    right -= 1
    
        def sortColors_v2(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            ## Idea: 2 pass. Count how many each 0, 1, 2 has happened
            ## Complexity
            ## Sample Data:
            ##     0 1 2 0 1 2 0
            ##     p           r
            ##       q
            ##     2 0
            count0, count1, count2 = 0, 0, 0
            for num in nums:
                if num == 0:
                    count0 += 1
                if num == 1:
                    count1 += 1
                if num == 2:
                    count2 += 1
    
            for i in xrange(len(nums)):
                if i < count0:
                    nums[i] = 0
                elif i < count0 + count1:
                    nums[i] = 1
                else:
                    nums[i] = 2
    
        def sortColors_v1(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            ## Idea: 2 pointer. 2 pass
            ## Complexity: Time O(n), Space O(1)
            length = len(nums)
            if length<=1:
                return
    
            # 1st pass
            for p in xrange(length):
                if nums[p] != 0:
                    break
            for q in range(p+1, length):
                if nums[q] == 0:
                    nums[q] = nums[p]
                    nums[p] = 0
                    p += 1
    
            # 2nd pass
            for p in xrange(length):
                if nums[p] == 2:
                    break
            for q in range(p+1, length):
                if nums[q] == 1:
                    nums[q] = nums[p]
                    nums[p] = 1
                    p += 1

More Reading:  
-   [Puzzle: First Missing Positive](http://brain.dennyzhang.com/missing-positive/)
-   [Kids Puzzles](http://brain.dennyzhang.com/tag/kids/)