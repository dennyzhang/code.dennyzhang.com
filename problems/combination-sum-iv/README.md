
# Leetcode: Combination Sum IV     :BLOG:Medium:

---

Combination Sum IV  

---

Similar Problems:  

-   [Combination Sum III](https://code.dennyzhang.com/combination-sum-iii)
-   [Review: Combinations and Permutations Problems](https://code.dennyzhang.com/review-combination)
-   Tag: [#combination](https://code.dennyzhang.com/tag/combination), [#classic](https://code.dennyzhang.com/tag/classic),  [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.  

Example:  

    nums = [1, 2, 3]
    target = 4
    
    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
    
    Note that different sequences are counted as different combinations.
    
    Therefore the output is 7.

Follow up:  

-   What if negative numbers are allowed in the given array?
-   How does it change the problem?
-   What limitation we need to add to the question to allow negative numbers?

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/combination-sum-iv)  

Credits To: [leetcode.com](https://leetcode.com/problems/combination-sum-iv/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/combination-sum-iv
    // Basic Ideas: dynamic programming
    // [1, 2, 3], 4
    // 1, 2, 3
    // 1 1, 2 1, 3 1, 1 2, 2 2, 1 3
    //   2:1, 3:2, 4:3
    // 1 1 1, 1 1 2, 1 1 3, 2 1 1....
    //   3:1, 4:3
    //
    // Complexity: Time ?, Space O(n)
    func combinationSum4(nums []int, target int) int {
        res := 0
        m := map[int]int{}
        for _, num := range nums {
    	if num > target { continue }
    	m[num] = 1
        }
        should_continue := true
        for should_continue {
    	m2 := map[int]int{}
    	for _, num := range nums {
    	    for p := range m {
    		if p+num<=target {
    		    m2[p+num] += m[p]
    		}
    	    }
    	}
    	if len(m2) == 0 {
    	    should_continue = false
    	} else {
    	    res += m[target]
    	    m = map[int]int{}
    	    for num := range m2 {
    		m[num] = m2[num]
    	    }
    	}
        }
        return res + m[target]
    }

