# Leetcode: Image Overlap     :BLOG:Medium:


---

Image Overlap  

---

Similar Problems:  
-   Tag: [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#array](https://code.dennyzhang.com/tag/array)

---

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)  

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.  

(Note also that a translation does not include any kind of rotation.)  

What is the largest possible overlap?  

Example 1:  

    Input: A = [[1,1,0],
                [0,1,0],
                [0,1,0]]
           B = [[0,0,0],
                [0,1,1],
                [0,0,1]]
    Output: 3
    Explanation: We slide A to right by 1 unit and down by 1 unit.

Notes:  

    - 1 <= A.length = A[0].length = B.length = B[0].length <= 30
    - 0 <= A[i][j], B[i][j] <= 1

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/image-overlap)  

Credits To: [leetcode.com](https://leetcode.com/problems/image-overlap/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/image-overlap
    // Basic Ideas:
    // Try A[0][0] for all points in B
    // Try B[0][0] for all points in A
    // Complexity: Time O(n^4), Space O(1)
    func largestOverlap(A [][]int, B [][]int) int {
        res, n := 0, len(A)
        for i:= 0; i<n; i++ {
            for j:=0; j<n; j ++ {
                count1, count2 := 0, 0
                for i1:=i; i1<n; i1++ {
                    for j1:=j; j1<n; j1++ {
                        i2,j2:=i1-i, j1-j
                        if A[i1][j1]==1 && A[i1][j1]==B[i2][j2]{
                            count1 += 1
                        }
                        if B[i1][j1]==1 && B[i1][j1]==A[i2][j2]{
                            count2 += 1
                        }
                    }
                }
                if count1>res { res = count1 }
                if count2>res { res = count2 }
            }
        }
        return res
    }