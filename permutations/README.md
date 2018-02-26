# Leetcode: Permutations     :BLOG:Basic:


---

Permutations  

---

Similar Problems:  
-   [Review: Classic Code Problems](https://brain.dennyzhang.com/review-classic)

---

Given a collection of distinct numbers, return all possible permutations.  

For example,  

    [1,2,3] have the following permutations:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/permutations)  

Credits To: [leetcode.com](https://leetcode.com/problems/permutations/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/permutations
    ## Basic Ideas: Insertion
    ##            1
    ##            12 -> 12; 21
    ##            123 -> 312, 132, 123; 321, 231, 213
    ###           1234 -> ...
    ## Complexity:
    import copy
    class Solution:
        def permute(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            if len(nums) == 0: return [[v]]
            return self.myPermute(nums[0:-1], nums[-1])
    
        def myPermute(self, nums, v):
            if len(nums) == 0: return [[v]]
            res = []
            l = self.myPermute(nums[0:-1], nums[-1])
            for sequence in l:
                for i in range(0, len(sequence)+1):
                    row = copy.deepcopy(sequence)
                    row.insert(i, v)
                    res.append(row)
            return res