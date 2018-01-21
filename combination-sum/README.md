# Leetcode: Combination Sum     :BLOG:Basic:


---

Combination Sum  

---

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.  

The same repeated number may be chosen from C unlimited number of times.  

Note:  
-   All numbers (including target) will be positive integers.
-   The solution set must not contain duplicate combinations.

    For example, given candidate set [2, 3, 6, 7] and target 7, 
    A solution set is: 
    [
      [7],
      [2, 2, 3]
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/combination-sum)  

Credits To: [leetcode.com](https://leetcode.com/problems/combination-sum/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def combinationSum(self, candidates, target):
            """
            :type candidates: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
            ## Idea:
            ## Complexity:
            ## 2 3 6 7, t=7
            ## v
            ## t/v, t/v - 1, t/v - 2, ...
            # TODO: improve this
            candidates = sorted(candidates)
            length = len(candidates)
            if length == 0:
                return []
            ret = []
            value = candidates[0]
            # print("target: %d, value: %d" % (target, value))
            for i in range(0, target/value+1):
                # print("here1 target: %d, value: %d, i: %d" % (target, value, i))
                if (target > i*value) and (length >= 2):
                    # print("here2 target: %d, value: %d, i: %d" % (target, value, i))
                    l1 = [value]*i
                    l2 = self.combinationSum(candidates[1:], target - i*value)
                    for item2 in l2:
                        ret.append(l1 + item2)
                else:
                    if target == i*value:
                        ret.append([value]*i)
            return ret