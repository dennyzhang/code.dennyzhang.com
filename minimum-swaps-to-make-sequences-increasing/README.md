# Leetcode: Minimum Swaps To Make Sequences Increasing     :BLOG:Medium:


---

Minimum Swaps To Make Sequences Increasing  

---

Similar Problems:  
-   [Review: Dynamic Programming Problems](https://brain.dennyzhang.com/review-dynamicprogramming)
-   Tag: [#dynamicprogramming](https://brain.dennyzhang.com/tag/dynamicprogramming), [#inspiring](https://brain.dennyzhang.com/tag/inspiring)

---

We have two integer sequences A and B of the same non-zero length.  

We are allowed to swap elements A[i] and B[i]. Note that both elements are in the same index position in their respective sequences.  

At the end of some number of swaps, A and B are both strictly increasing.  

    (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.  

Example:  

    Input: A = [1,3,5,4], B = [1,2,3,7]
    Output: 1
    Explanation: 
    Swap A[3] and B[3].  Then the sequences are:
    A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
    which are both strictly increasing.

Note:  

-   A, B are arrays with the same length, and that length will be in the range [1, 1000].
-   A[i], B[i] are integer values in the range [0, 2000].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/minimum-swaps-to-make-sequences-increasing)  

Credits To: [leetcode.com](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/minimum-swaps-to-make-sequences-increasing
    ## Basic Ideas: dynamic programming
    ##
    ##    If examining two adjacent columns, there are only 2 combinations!
    ##     
    ##    dp[i][2]: swap or don't swap current item
    ##
    ## Complexity: Time O(n), Space O(n)
    class Solution:
        def minSwap(self, A, B):
            """
            :type A: List[int]
            :type B: List[int]
            :rtype: int
            """
            import sys
            length = len(A)
            dp = [[sys.maxsize, sys.maxsize] for i in range(length)]
            dp[0] = [0, 1]
            for i in range(1, length):
                # case1: don't swap
                if A[i]>A[i-1] and B[i]>B[i-1]:
                    dp[i][0] = min(dp[i][0], dp[i-1][0])
                    dp[i][1] = min(dp[i][1], dp[i-1][1] + 1)
    
                # case2: swap
                if A[i]>B[i-1] and B[i]>A[i-1]:
                    dp[i][0] = min(dp[i][0], dp[i-1][1])
                    dp[i][1] = min(dp[i][1], dp[i-1][0] + 1) 
            return min(dp[-1][0], dp[-1][1])