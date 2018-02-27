# Leetcode: Combination Sum II     :BLOG:Hard:


---

Combination  

---

Similar Problems:  
-   [Review: Combinations and Permutations Problems](https://brain.dennyzhang.com/review-combination), [Tag: #combination](https://brain.dennyzhang.com/tag/combination)

---

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.  

Each number in C may only be used once in the combination.  

Note:  
-   All numbers (including target) will be positive integers.
-   The solution set must not contain duplicate combinations.

    For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
    A solution set is: 
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/combination-sum-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/combination-sum-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/combination-sum-ii
    ## Basic Ideas: Sort the list with descending order
    ##
    ## Complexity: Time O(n*n), Space O(n)
    class Solution:
        def combinationSum2(self, candidates, target):
            """
            :type candidates: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
            if len(candidates) == 0: return []
            candidates = sorted(candidates)
            length = len(candidates)
            res = []
            for i in range(length):
                if candidates[i] > target: continue
                if candidates[i] == target:
                    if [target] not in res: res.append([target])
                    continue
                # try to start the result with candidates[i]
                l = self.combinationSum2(candidates[i+1:], target - candidates[i])
                for element in l:
                    if not [candidates[i]]+element in res:
                        res.append([candidates[i]]+element)
    
            return res