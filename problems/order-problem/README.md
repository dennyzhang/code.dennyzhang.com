
# LintCode: Order Problem     :BLOG:Medium:

---

Order Problem  

---

Similar Problems:  

-   [Ones and Zeroes](https://code.dennyzhang.com/ones-and-zeroes)
-   [Review: Knapsack Problems](https://code.dennyzhang.com/review-knapsack)
-   Tag: [#classic](https://code.dennyzhang.com/tag/classic), [#knapsack](https://code.dennyzhang.com/tag/knapsack)

---

Description  

    There is now an order with demand for n items, and the demand for the i-th item is order[i]. The factory has m production modes. Each production mode is shaped like [p[1],p[2],...p[n]], that is, produce p[1] first items, p[2] second items... You can use multiple production modes. Please tell me how many items do not meet the demand at least in the case of not exceeding the demand of any kind of items?

-   1 <= n, m <= 7
-   1 <= order[i] <= 10
-   0 <= pattern[i][j] <= 10

    Example
    Given order=[2,3,1], pattern=[[2,2,0],[0,1,1],[1,1,0]] , return 0.
    
    Explanation:
    Use [0,1,1] once, [1,1,0] twice, remaining [0,0,0].

    Given order=[2,3,1], pattern=[[2,2,0]] , return 2.
    
    Explanation:
    Use [2,2,0] once, remaining [0,1,1].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/order-problem)  

Credits To: [lintcode.com](https://www.lintcode.com/problem/order-problem/description)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: BFS

[#knapsack](https://code.dennyzhang.com/tag/knapsack) problem, [Ones and Zeroes](https://code.dennyzhang.com/ones-and-zeroes)  

    // Blog link: https://code.dennyzhang.com/order-problem
    // Basic Ideas: BFS
    // Complexity:
    type Item struct {
      sum int
      pattern []int
    }
    
    func getMinRemaining (order []int, pattern [][]int) int {
        total_sum := 0
        for _, v := range order { total_sum += v }
        sum_list := make([]int, len(pattern))
    
        res := total_sum
        queue := []Item{}
        for i, p := range pattern {
    	could_match := true
    	for j, v:= range p {
    	    sum_list[i] += v
    	    if v > order[j] { could_match = false }
    	}
    	if sum_list[i]!=0 && could_match {
    	    queue = append(queue, Item{sum_list[i], p})
    	    if res > total_sum - sum_list[i] { res = total_sum - sum_list[i] }
    	}
        }
    
        for len(queue) != 0 {
    	l := []Item{}
    	for _, item := range queue {
    	    for i, p := range pattern {
    		j := 0
    		newPattern := []int{}
    		diff := total_sum - (sum_list[i] + item.sum)
    		if diff >= 0 {
    		    for j<len(order) && p[j]+item.pattern[j]<=order[j] {
    			newPattern = append(newPattern, p[j]+item.pattern[j])
    			j++
    		    }
    		}
    		if j == len(order) {
    		    if diff ==0 { return 0 }
    		    l = append(l, Item{sum_list[i] + item.sum, newPattern})
    		    if (diff < res) { res = diff }
    
    		}
    	    }
    	}
    	queue = []Item{}
    	for _, item := range l { queue = append(queue, item) }
        }
        return res
    }

