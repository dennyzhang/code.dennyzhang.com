# Leetcode: Target Sum     :BLOG:Medium:


---

Target Sum  

---

Similar Problems:  
-   [Expression Add Operators](https://code.dennyzhang.com/expression-add-operators)
-   [Review: BFS Problems](https://code.dennyzhang.com/review-bfs)
-   Tag: [#bfs](https://code.dennyzhang.com/tag/bfs)

---

You are given a list of non-negative integers, a1, a2, &#x2026;, an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.  

Find out how many ways to assign symbols to make sum of integers equal to target S.  

Example 1:  

    Input: nums is [1, 1, 1, 1, 1], S is 3. 
    Output: 5
    Explanation: 
    
    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3
    
    There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:  
-   The length of the given array is positive and will not exceed 20.
-   The sum of elements in the given array will not exceed 1000.
-   Your output answer is guaranteed to be fitted in a 32-bit integer.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/target-sum)  

Credits To: [leetcode.com](https://leetcode.com/problems/target-sum/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/target-sum
    // Basic Ideas: BFS + hashmap
    // Complexity: Time O(pow(2, n)), Space O(1)
    //   The value would be in between -1000 and 1000
    //   Thus Space is O(1)
    func findTargetSumWays(nums []int, S int) int {
        m := make(map[int]int)
        m[0] = 1
        for _, num := range nums {
            m2 := make(map[int]int)
            for v := range m {
                m2[v+num] += m[v]
                m2[v-num] += m[v]
            }
            m = m2
        }
        return m[S]
    }