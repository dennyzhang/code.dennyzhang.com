# Leetcode: Combination Sum II     :BLOG:Hard:


---

0-1 bags  

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

Credits To: [Leetcode.com](https://leetcode.com/problems/combination-sum-ii/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def combinationSum2(self, candidates, target):
            """
            :type candidates: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
            ## Basic Ideas: sort the list, then 0-1 bag
            ## Complexity: Time ? Space ?
            ## Assumptions:
            ## Sample Data:
            ##      1 1 2 5 6 7 10
            candidates = sorted(candidates)
            return self.mycombinationSum2(candidates, target)
    
        def mycombinationSum2(self, candidates, target):
            length = len(candidates)
            if length == 0:
                return 
            res = 
            v = candidates[0]
            if target >= v:
                # choose
                if target == v:
                    if [v] not in res:
                        res.append([v])
                else:
                    for item in self.mycombinationSum2(candidates[1:], target - v):
                        if [v] + item not in res:
                            res.append([v]+item)
    
                for item in self.mycombinationSum2(candidates[1:], target):
                    if item not in res:
                        res.append(item)
            else:
                for item in self.mycombinationSum2(candidates[1:], target):
                    if item not in res:
                        res.append(item)
            return res
    
    s = Solution()
    print s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)

More Reading:  
-   [Leetcode: Valid Triangle Number](http://brain.dennyzhang.com/triangle-number/)