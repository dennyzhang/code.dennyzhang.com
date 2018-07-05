
# Leetcode: Ones and Zeroes     :BLOG:Medium:

---

Ones and Zeroes  

---

-   [LintCode: Order Problem](https://code.dennyzhang.com/order-problem)
-   [Review: Knapsack Problems](https://code.dennyzhang.com/review-knapsack)
-   Tag: [#knapsack](https://code.dennyzhang.com/tag/knapsack), [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.  

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.  

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.  

Note:  

1.  The given numbers of 0s and 1s will both not exceed 100
2.  The size of given string array won't exceed 600.

Example 1:  

    Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
    Output: 4
    
    Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10,"0001","1","0"

Example 2:  

    Input: Array = {"10", "0", "1"}, m = 1, n = 1
    Output: 2
    
    Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/ones-and-zeroes)  

Credits To: [leetcode.com](https://leetcode.com/problems/ones-and-zeroes/description/)  

Leave me comments, if you have better ways to solve.  

---

Similar problem: [LintCode: Order Problem](https://code.dennyzhang.com/order-problem)  

    // Blog link: https://code.dennyzhang.com/ones-and-zeroes
    // Basic Ideas: dynamic programming
    // Complexity: 
    type Entity struct {
        count_0, count_1 int
    }
    
    func findMaxForm(strs []string, m int, n int) int {
        res := 0
        hashmap := make(map[Entity]int)
        for _, p := range strs {
    	count_0, count_1 := 0, 0
    	for _, ch := range p {
    	    if ch == '0' { 
    		count_0 += 1
    	    } else {
    		count_1 += 1
    	    }
    	}
    	if count_0 > m || count_1>n { continue }
    	// add current item
    	v := Entity{count_0, count_1}
    	hashmap_tmp := make(map[Entity]int)
    	hashmap_tmp[v] = 1
    	if hashmap_tmp[v] > res { res = hashmap_tmp[v] }
    	// loop original map
    	for q := range hashmap {
    	    // add original item
    	    if hashmap[q] > hashmap_tmp[q] { 
    		hashmap_tmp[q] = hashmap[q]
    	    }
    	    // add new item
    	    if q.count_0+count_0>m || q.count_1+count_1>n { continue }
    	    r := Entity{q.count_0+count_0, q.count_1+count_1}
    	    if hashmap[q] + 1 > hashmap_tmp[r] {
    		hashmap_tmp[r] = hashmap[q] + 1
    	    }
    	    if hashmap_tmp[r]>res { res = hashmap_tmp[r] }
    	}
    	// copy map
    	hashmap = make(map[Entity]int)
    	for q:= range hashmap_tmp {
    	    hashmap[q] = hashmap_tmp[q]
    	}
        }
        return res
    }

