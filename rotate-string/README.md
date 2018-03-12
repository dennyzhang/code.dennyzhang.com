# Leetcode: Rotate String     :BLOG:Basic:


---

Rotate String  

---

Similar Problems:  
-   [Repeated String Match](https://brain.dennyzhang.com/repeated-string-match)
-   [Tag: #string](https://brain.dennyzhang.com/tag/string)

---

We are given two strings, A and B.  

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.  

Example 1:  

    Input: A = 'abcde', B = 'cdeab'
    Output: true

Example 2:  

    Input: A = 'abcde', B = 'abced'
    Output: false

Note:  

-   A and B will have length at most 100.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/rotate-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/rotate-string/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/rotate-string
    class Solution:
        def rotateString(self, A, B):
            """
            :type A: str
            :type B: str
            :rtype: bool
            """
            return len(A) == len(B) and B in A + A