
# Leetcode: New 21 Game     :BLOG:Medium:

---

New 21 Game  

---

Similar Problems:  

-   [Climbing Stairs](https://code.dennyzhang.com/climbing-stairs)
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming), [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#game](https://code.dennyzhang.com/tag/game), [#possibilities](https://code.dennyzhang.com/tag/possibilities)

---

Alice plays the following game, loosely based on the card game "21".  

Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.  

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?  

Example 1:  

    Input: N = 10, K = 1, W = 10
    Output: 1.00000
    Explanation:  Alice gets a single card, then stops.

Example 2:  

    Input: N = 6, K = 1, W = 10
    Output: 0.60000
    Explanation:  Alice gets a single card, then stops.
    In 6 out of W = 10 possibilities, she is at or below N = 6 points.

Example 3:  

    Input: N = 21, K = 17, W = 10
    Output: 0.73278

Note:  

1.  0 <= K <= N <= 10000
2.  1 <= W <= 10000
3.  Answers will be accepted as correct if they are within 10^-5 of the correct answer.
4.  The judging time limit has been reduced for this question.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/new-21-game)  

Credits To: [leetcode.com](https://leetcode.com/problems/new-21-game/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/new-21-game
    // Basic Ideas: dynamic programming
    // dp(i): The possibility of get i
    //
    //      O ... O + b
    //                b in [1, W]
    //
    // dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]+... + dp[i-W])/W
    //
    // result:
    //         dp[K]+dp[K+1]+...dp[N]
    //
    // Complexity: Time O(N), Space O(N)
    func new21Game(N int, K int, W int) float64 {
        if (K == 0 || N >= K + W) { return 1.0 }
        dp := make([]float64, N+1)
        dp[0] = 1
        var sum, res float64
        sum, res = 1, 0
        for i:=1; i<=N; i++ {
    	dp[i] = sum/float64(W)
    	if i<K {
    	    sum += dp[i]
    	} else {
    	    res += dp[i] 
    	}
    	if i-W>=0 {
    	    sum -= dp[i-W]
    	}
        }
        return res
    }

