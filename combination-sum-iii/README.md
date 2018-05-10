# Leetcode: Combination Sum III     :BLOG:Medium:


---

Combination Sum III  

---

Similar Problems:  
-   [Combination Sum IV](https://code.dennyzhang.com/combination-sum-iv)
-   [Review: Combinations and Permutations Problems](https://code.dennyzhang.com/review-combination)
-   Tag: [#combination](https://code.dennyzhang.com/tag/combination)

---

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.  

    Example 1:
    
    Input: k = 3, n = 7
    
    Output:
    
    [[1,2,4]]

    Example 2:
    
    Input: k = 3, n = 9
    
    Output:
    
    [[1,2,6], [1,3,5], [2,3,4]]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/combination-sum-iii)  

Credits To: [leetcode.com](https://leetcode.com/problems/combination-sum-iii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/combination-sum-iii
    class Solution(object):
        def combinationSum3(self, k, n):
            """
            :type k: int
            :type n: int
            :rtype: List[List[int]]
            """