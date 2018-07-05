
# Leetcode: Consecutive Numbers Sum     :BLOG:Medium:

---

Consecutive Numbers Sum  

---

Similar Problems:  

-   [Review: sqrt Problems](https://code.dennyzhang.com/review-sqrt)
-   Tag: [#math](https://code.dennyzhang.com/tag/math), [#sqrt](https://code.dennyzhang.com/tag/sqrt)

---

Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?  

Example 1:  

    Input: 5
    Output: 2
    Explanation: 5 = 5 = 2 + 3

Example 2:  

    Input: 9
    Output: 3
    Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

Example 3:  

    Input: 15
    Output: 4
    Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Note: 1 <= N <= 10 ^ 9.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/consecutive-numbers-sum)  

Credits To: [leetcode.com](https://leetcode.com/problems/consecutive-numbers-sum/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/consecutive-numbers-sum
    // Basic Ideas:
    //
    // How many numbers it can be divided?
    //   i, i+1, i+2, ..., i+k
    //   n = (i+i+k)*k/2
    //   So n=i*k+k*k/2. Thus k*k<n*2
    //
    // How to examine whether N can be divided into k consecutive numbers?
    //   If k is odd
    //        the numbers have one central element.
    //        If N can be divided into k numbers, the central element must be N/k
    //        So N%k must equal 0. And we can choose N/k as the central element
    //   If k is even
    //        The numbers will have two central elements: (v, v+1)
    //        Let's say q=k/2
    //        We can group k elements into q groups. (i, i+k), (i+1, i+k-1), ...
    //        So N%q must equal 0, and N/q must be odd. Here we can choose v= (2*N/k-1)/2
    // Complexity: Time sqrt(n), Space O(1)
    func consecutiveNumbersSum(N int) int {
        res := 0
        for i:=1; i*i<2*N; i++ {
    	if i%2 == 1 {
    	    if N%i == 0 {
    		res += 1
    	    }
    	} else {
    	    q := int(i/2)
    	    if N%q == 0 && (N/q) %2==1 {
    		res += 1
    	    }
    	}
        }
        return res
    }

