
# Leetcode: Peak Index in a Mountain Array     :BLOG:Basic:

---

Peak Index in a Mountain Array  

---

Similar Problems:  

-   [Longest Mountain in Array](https://code.dennyzhang.com/longest-mountain-in-array)
-   Tag: [#array](https://code.dennyzhang.com/tag/array), [#mountain](https://code.dennyzhang.com/tag/mountain)

---

Let's call an array A a mountain if the following properties hold:  

-   A.length >= 3
-   There exists some 0 < i < A.length - 1 such that A[0] < A[1] < &#x2026; A[i-1] < A[i] > A[i+1] > &#x2026; > A[A.length - 1]

Given an array that is definitely a mountain, return any i such that A[0] < A[1] < &#x2026; A[i-1] < A[i] > A[i+1] > &#x2026; > A[A.length - 1].  

Example 1:  

    Input: [0,1,0]
    Output: 1

Example 2:  

    Input: [0,2,1,0]
    Output: 1

Note:  

-   3 <= A.length <= 10000
-   0 <= A[i] <= 10^6
-   A is a mountain, as defined above.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/peak-index-in-a-mountain-array)  

Credits To: [leetcode.com](https://leetcode.com/problems/peak-index-in-a-mountain-array/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/peak-index-in-a-mountain-array
    // Basic Ideas: Too straightforward
    // Complexity: Time O(n), Space O(1)
    func peakIndexInMountainArray(A []int) int {
        for i:=1; i<len(A)-1; i++ {
    	if A[i]>A[i-1] && A[i]>A[i+1] {
    	    return i
    	}
        }
        return -1
    }

