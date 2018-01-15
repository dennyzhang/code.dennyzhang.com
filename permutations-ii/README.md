# Leetcode: Permutations II     :BLOG:Basic:


---

Permutations II  

---

Given a collection of numbers that might contain duplicates, return all possible unique permutations.  

    For example,
    [1,1,2] have the following unique permutations:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/majority-element-ii)  

Credits To: [Leetcode.com](https://leetcode.com/problems/majority-element-ii/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def permuteUnique(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            nums.sort()
            return self._permuteUnique(nums)
    
        def _permuteUnique(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            length = len(nums)
            if length == 0:
                return 
            if length == 1:
                return [nums]
            res = 
            for i in xrange(length):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                l = self._permuteUnique(nums[:i] + nums[i+1:])
                for element in l:
                    element = [nums[i]] + element
                    res.append(element)
            return res