# Leetcode: Longest Mountain in Array     :BLOG:Medium:


---

Longest Mountain in Array  

---

Similar Problems:  
-   Tag: [#array](https://code.dennyzhang.com/tag/array)

---

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:  

    B.length >= 3
    There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
    (Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.  

Return 0 if there is no mountain.  

Example 1:  

    Input: [2,1,4,7,3,2,5]
    Output: 5
    Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:  

    Input: [2,2,2]
    Output: 0
    Explanation: There is no mountain.

Note:  

1.  0 <= A.length <= 10000
2.  0 <= A[i] <= 10000

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/longest-mountain-in-array)  

Credits To: [leetcode.com](https://leetcode.com/problems/longest-mountain-in-array/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: XXX

    // Blog link: https://code.dennyzhang.com/longest-mountain-in-array
    // Basic Ideas:
    // Find the top of the mountains. Then keep looking both sides
    // Complexity: Time O(n), Space O(n)
    
    func longestMountain(A int) int {
        res := 0
        for i:=1; i<len(A)-1; i++ {
            if A[i-1]<A[i] && A[i]>A[i+1] {
                j, k := i-1, i+1
                for j-1>=0 && A[j-1]<A[j] { j-- }
                for k+1<len(A) && A[k]>A[k+1] { k++ }
                if k-j+1 > res { res = k-j+1 }
            }
        }
        return res
    }