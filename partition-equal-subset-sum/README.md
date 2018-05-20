# Leetcode: Partition Equal Subset Sum     :BLOG:Medium:


---

Partition Equal Subset Sum  

---

Similar Problems:  
-   [Partition Equal Subset Sum](https://code.dennyzhang.com/partition-equal-subset-sum)
-   [Review: Combinations and Permutations Problems](https://code.dennyzhang.com/review-combination)
-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming)
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming), [#combination](https://code.dennyzhang.com/tag/combination)

---

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.  

Note:  
1.  Each of the array element will not exceed 100.
2.  The array size will not exceed 200.

    Example 1:
    
    Input: [1, 5, 11, 5]
    
    Output: true
    
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

    Example 2:
    
    Input: [1, 2, 3, 5]
    
    Output: false
    
    Explanation: The array cannot be partitioned into equal sum subsets.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/partition-equal-subset-sum)  

Credits To: [leetcode.com](https://leetcode.com/problems/partition-equal-subset-sum/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/partition-equal-subset-sum
    ## Basic Ideas: hashmap
    ##
    ## Complexity: Time O(n), Space O(1)
    ##     Total sum would be smaller than 20000.
    ##     So the size of hashmap would be smaller than sum/2. That's 10000
    ##
    class Solution(object):
        def canPartition(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            import copy
            sum_value = sum(nums)
            if sum_value%2 != 0: return False
            target = sum_value/2
            print(sum_value, target)
            value_set = set([])
            for num in nums:
                tmp_set = copy.deepcopy(value_set)
                for v in value_set:
                    if v+num == target: return True
                    if v+num < target:
                        tmp_set.add(v+num)
                if num == target: return True
                if num < target:
                    tmp_set.add(num)
                value_set = tmp_set
            return False