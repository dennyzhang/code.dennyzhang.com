# Leetcode: Most Profit Assigning Work     :BLOG:Medium:


---

Most Profit Assigning Work  

---

Similar Problems:  
-   Tag: [#binarysearch](https://code.dennyzhang.com/tag/binarysearch), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job.  

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i].  

Every worker can be assigned at most one job, but one job can be completed multiple times.  

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.  

What is the most profit we can make?  

Example 1:  

    Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
    Output: 100
    Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.

Notes:  

-   1 <= difficulty.length = profit.length <= 10000
-   1 <= worker.length <= 10000
-   difficulty[i], profit[i], worker[i]  are in range [1, 10^5]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/most-profit-assigning-work)  

Credits To: [leetcode.com](https://leetcode.com/problems/most-profit-assigning-work/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/most-profit-assigning-work
    // Basic Ideas: dynamic programming + binarysearch
    //
    // Complexity: Time O(n*log(n)), Space O(n)
    func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
        m := make(map[int]int)
        for i, d := range difficulty {
            v, status := m[d]
            if status == false {
                m[d] = profit[i]
            } else {
                if v<profit[i] {m[d]=profit[i]}
            }
        }
    
        sort.Ints(difficulty[:])
        for i := 0; i<len(profit); i++ {
            v, _ := m[difficulty[i]]
            profit[i] = v
        }
    
        // get most profit values
        dp := make([]int, len(difficulty))
        dp[0] = profit[0]
        for i, _ := range difficulty {
            if i == 0 { continue }
            dp[i] = profit[i]
            if dp[i] < dp[i-1] { dp[i] = dp[i-1] }
        }
    
        res := 0
        // binarysearch: find the first no smaller value
        for _, w := range worker{
            item := 0
            left, right := 0, len(difficulty)
            for left<right {
                mid := left + int((right-left)/2)
                if difficulty[mid] == w {
                    item = dp[mid]
                    break
                } else{
                    if difficulty[mid] > w {
                       right = mid
                    } else {
                        left = mid + 1
                    }
                }
          }
          if item == 0 {
              if left != 0 { item = dp[left-1] }
          }
          res += item
        }
        return res
    }