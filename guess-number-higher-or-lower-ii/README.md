# Leetcode: Guess Number Higher or Lower II     :BLOG:Amusing:


---

Guess Number Higher or Lower  

---

Similar Problems:  
-   [Review: Game Problems](https://code.dennyzhang.com/review-game)
-   Tag: [#game](https://code.dennyzhang.com/tag/game), [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#dp2order](https://code.dennyzhang.com/tag/dp2order), [#minmax](https://code.dennyzhang.com/tag/minmax), [#classic](https://code.dennyzhang.com/tag/classic)

---

We are playing the Guess Game. The game is as follows:  

I pick a number from 1 to n. You have to guess which number I picked.  

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.  

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.  

Example:  

    n = 10, I pick 8.
    
    First round:  You guess 5, I tell you that it's higher. You pay $5.
    Second round: You guess 7, I tell you that it's higher. You pay $7.
    Third round:  You guess 9, I tell you that it's lower. You pay $9.
    
    Game over. 8 is the number I picked.
    
    You end up paying $5 + $7 + $9 = $21.

Given a particular n >= 1, find out how much money you need to have to guarantee a win.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/guess-number-higher-or-lower-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/guess-number-higher-or-lower-ii
    // Basic Ideas: Dynamic Programming
    //
    // f(i, j) -> money we need to gurantee a win for the range of [i, j]
    //    We will have to start by picking one, let's say it's k.
    //    Then the cost is: k + max(f(i, k-1), f(k+1, j))
    //
    // From bottom to up, from left to right, we can get f(1, n)
    // Complexity: Time O(n*n*n), Space O(n*n)
    func getMoneyAmount(n int) int {
        dp := make([][]int, n+1)
        for i:=0; i<n+1; i++ { dp[i] = make([]int, n+1) }
        for i:=n-1; i>=1; i-- {
            // Range of i:j
            for j := i+1; j<=n; j++ {
                cost, mincost := 0, 1<<31 - 1
                for k:=i; k<=j; k++ {
                    cost = k
                    r1, r2 := 0, 0
                    if k!=i { r1 = dp[i][k-1] }
                    if k!=j { r2 = dp[k+1][j] }
                    if r1 > r2 {
                        cost += r1
                    } else {
                        cost += r2
                    }
                    if mincost > cost { mincost = cost }
                }
                dp[i][j] = mincost
            }
        }
        return dp[1][n]
    }