
# Leetcode: Predict the Winner     :BLOG:Medium:

---

Predict the Winner  

---

Similar Problems:  

-   [Target Sum](https://code.dennyzhang.com/target-sum)
-   [Review: minmax Problems](https://code.dennyzhang.com/review-minmax)
-   [Review: Game Problems](https://code.dennyzhang.com/review-game)
-   Tag: [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#game](https://code.dennyzhang.com/tag/game), [#minmax](https://code.dennyzhang.com/tag/minmax), [#dp2order](https://code.dennyzhang.com/tag/dp2order)

---

Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.  

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.  

Example 1:  

    Input: [1, 5, 2]
    Output: False
    Explanation: Initially, player 1 can choose between 1 and 2. 
    If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
    So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
    Hence, player 1 will never be the winner and you need to return False.

Example 2:  

    Input: [1, 5, 233, 7]
    Output: True
    Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
    Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Note:  

1.  1 <= length of the array <= 20.
2.  Any scores in the given array are non-negative integers and will not exceed 10,000,000.
3.  If the scores of both players are equal, then player 1 is still the winner.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/predict-the-winner)  

Credits To: [leetcode.com](https://leetcode.com/problems/predict-the-winner/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/predict-the-winner
    // Basic Ideas: Dynamic Programming
    //
    // f(i, j): max value we can get, if we start with [i, j]
    //     if we choose i, we get sum[i:j]-f(i+1, j)
    //     if we choose j, we get sum[i:j]-f(i, j-1)
    //
    // Complexity: Time O(n*n), Space O(n*n)
    func PredictTheWinner(nums []int) bool {
        sums := make([]int, len(nums))
        sum := 0
        for i, num := range nums {
    	sum += num
    	sums[i] = sum
        }
        dp := make([][]int, len(nums))
        for i, _ := range dp { dp[i] = make([]int, len(nums))}
        // from bottom to up
        for i:=len(nums)-1; i>=0; i-- {
    	// from left to right
    	for j:=i; j<len(nums); j++ {
    	    if i==j {
    		// base case
    		dp[i][j] = nums[i]
    		continue
    	    }
    	    // choose from [i: j]
    	    v1, v2 := 0, 0
    	    sum = sums[j]-sums[i]+nums[i]
    	    v1 = sum - dp[i+1][j]
    	    v2 = sum - dp[i][j-1]
    	    if v1>v2 {
    		dp[i][j] = v1
    	    } else {
    		dp[i][j] = v2
    	    }
    	}
        }
        return dp[0][len(nums)-1]*2>=sums[len(nums)-1]
    }

