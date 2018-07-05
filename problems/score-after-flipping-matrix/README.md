# Leetcode: Score After Flipping Matrix     :BLOG:Medium:


---

Score After Flipping Matrix  

---

Similar Problems:  

-   Tag: [#array](https://code.dennyzhang.com/tag/array)

---

We have a two dimensional matrix A where each value is 0 or 1.  

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.  

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.  

Return the highest possible score.  

Example 1:  

    Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    Output: 39
    Explanation:
    Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
    0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Note:  

1.  1 <= A.length <= 20
2.  1 <= A<a id="fnr.1" name="fnr.1" class="footref" href="#fn.1">[1]</a>.length <= 20
3.  A[i][j] is 0 or 1.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/score-after-flipping-matrix)  

Credits To: [leetcode.com](https://leetcode.com/problems/score-after-flipping-matrix/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/score-after-flipping-matrix
    // Basic Ideas:
    //   Make sure the first column is all 1, by changing rows
    //   The check column by column. This time we check columns.
    //     Our target is to have maximum 1s
    //     If current column has equal 0s and 1s, should I swap?
    //     It doesn't matter
    // Complexity: Time O(n*m), Space O(1)
    import "math"
    func matrixScore(A int) int {
        row_count, col_count := len(A), len(A[0])
        res, power := 0, int(math.Pow(2, float64(col_count-1)))
        // Change first column
        res, power = res+row_count*power, power/2
        for i:=0; i<row_count; i++{
            if A[i][0] == 0 {
                for j:=0; j<col_count; j++ {
                    A[i][j] = 1-A[i][j]
                }
            }
        }
        // check other columns
        for j:=1; j<col_count; j++ {
            count := 0
            for i:=0; i<row_count; i++ {
                if A[i][j] == 1 { count++ }
            }
            if count < row_count-count { count = row_count-count }
            res, power = res+count*power, power/2
        }
        return res
    }

<div id="footnotes">
<p class="footnotes">Footnotes: </p>
<div id="text-footnotes" style="font-size:14px">

<div class="footdef"><a id="fn.1" name="fn.1" class="footnum" href="#fnr.1">[1]</a> <p>DEFINITION NOT FOUND.</p></div>


</div>
</div>