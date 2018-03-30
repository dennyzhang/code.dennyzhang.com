# Leetcode: Sparse Matrix Multiplication     :BLOG:Medium:


---

Sparse Matrix Multiplication  

---

Similar Problems:  
-   [Review: Math Problems](https://brain.dennyzhang.com/review-math)
-   [Review: Problems With Many Details](https://brain.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://brain.dennyzhang.com/tag/manydetails), [#math](https://brain.dennyzhang.com/tag/math)

---

Given two sparse matrices A and B, return the result of AB.  

You may assume that A's column number is equal to B's row number.  

Example:  

    A = [
      [ 1, 0, 0],
      [-1, 0, 3]
    ]
    
    B = [
      [ 7, 0, 0 ],
      [ 0, 0, 0 ],
      [ 0, 0, 1 ]
    ]
    
    
         |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
    AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                      | 0 0 1 |

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/sparse-matrix-multiplication)  

Credits To: [leetcode.com](https://leetcode.com/problems/sparse-matrix-multiplication/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/sparse-matrix-multiplication
    ## Basic Ideas:
    ##
    ## Complexity:
    class Solution:
        def multiply(self, A, B):
            """
            :type A: List[List[int]]
            :type B: List[List[int]]
            :rtype: List[List[int]]
            """
            if len(A) == 0 or len(B) == 0: return []
            # reverse B
            B2 = [[None for j in range(len(B))] for i in range(len(B[0]))]
            for i in range(len(B)):
                for j in range(len(B[0])):
                    B2[j][i] = B[i][j]
    
            C = [[0 for j in range(len(B[0]))] for i in range(len(A))]
            for i in range(len(A)):
                if A[i] == [0]*len(A[0]): continue
                for j in range(len(B[0])):
                    if B2[j] == [0]*len(B2[0]): continue
                    for k in range(len(A[0])):
                        C[i][j] += A[i][k]*B[k][j]
            return C