
# Leetcode: Binary Gap     :BLOG:Basic:

---

Binary Gap  

---

Similar Problems:  

-   Tag: [#string](https://code.dennyzhang.com/tag/string)

---

Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.  

If there aren't two consecutive 1's, return 0.  

Example 1:  

    Input: 22
    Output: 2
    Explanation: 
    22 in binary is 0b10110.
    In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
    The first consecutive pair of 1's have distance 2.
    The second consecutive pair of 1's have distance 1.
    The answer is the largest of these two distances, which is 2.

Example 2:  

    Input: 5
    Output: 2
    Explanation: 
    5 in binary is 0b101.

Example 3:  

    Input: 6
    Output: 1
    Explanation: 
    6 in binary is 0b110.

Example 4:  

    Input: 8
    Output: 0
    Explanation: 
    8 in binary is 0b1000.
    There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.

Note:  

-   1 <= N <= 10^9

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/binary-gap)  

Credits To: [leetcode.com](https://leetcode.com/problems/binary-gap/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/binary-gap
    // Basic Ideas:
    // From right to left
    // Complexity: Time O(1), Space O(1)
    func binaryGap(N int) int {
        distance, max_distance := 0, 0
        for N != 0 {
    	// 0b10110
    	if N%2 == 1 {
    	    if distance > max_distance { max_distance = distance }
    	    distance = 1
    	} else {
    	    if distance != 0 { distance++ }
    	}
    	N = N/2
        }
        return max_distance
    }

