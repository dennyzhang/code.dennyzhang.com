# Leetcode: Subsets II     :BLOG:Medium:


---

Subsets II  

---

Similar Problems:  
-   [Subsets](https://code.dennyzhang.com/subsets)
-   [Letter Case Permutation](https://code.dennyzhang.com/letter-case-permutation)
-   [Review: Combinations and Permutations Problems](https://code.dennyzhang.com/review-combination), [Tag: #combination](https://code.dennyzhang.com/tag/combination)

---

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).  

Note: The solution set must not contain duplicate subsets.  

    For example,
    If nums = [1,2,2], a solution is:
    
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/subsets-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/subsets-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/subsets-ii
    ## Basic Ideas:
    ##
    ## Complexity:
    class Solution:
        def subsetsWithDup(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            length = len(nums)
            if length == 0: return [[]]
            res = []
            for element in self.subsetsWithDup(nums[1:]):
                if element not in res: res.append(element)
    
                element2 = sorted([nums[0]] + element)
                if element2 not in res: res.append(element2)
            return res