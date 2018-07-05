
# Leetcode: Transpose Matrix     :BLOG:Basic:

---

Transpose Matrix  

---

Similar Problems:  

-   Tag: [#array](https://code.dennyzhang.com/tag/array)

---

Given a matrix A, return the transpose of A.  

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.  

Example 1:  

    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:  

    Input: [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]

Note:  

    1. 1 <= A.length <= 1000
    2. 1 <= A[0].length <= 1000

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/transpose-matrix)  

Credits To: [leetcode.com](https://leetcode.com/problems/transpose-matrix/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/transpose-matrix
    // Basic Ideas:
    // Complexity: Time O(n*m), Space O(1)
    func transpose(A [][]int) [][]int {
        if len(A) == 0 { return [][]int{} }
        row_count, col_count := len(A), len(A[0])
        res := make([][]int, col_count)
        for i, _ := range res { res[i] = make([]int, row_count) }
    
        for j:= 0; j<col_count; j++ {
    	for i:=0; i<row_count; i++ {
    	    res[j][i] = A[i][j]
    	}
        }
        return res
    }

