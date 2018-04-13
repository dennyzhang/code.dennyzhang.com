# Leetcode: Maximal Rectangle     :BLOG:Hard:


---

Maximal Rectangle  

---

Similar Problems:  
-   [Leetcode: Largest Rectangle in Histogram](https://code.dennyzhang.com/largest-rectangle-in-histogram)
-   [Review: Monotone Stack Or Monotone Queue Problems](https://code.dennyzhang.com/review-monotone), Tag: [monotone](https://code.dennyzhang.com/tag/monotone)
-   [Review: Rectangle Problems](https://code.dennyzhang.com/review-rectangle), Tag: [#rectangle](https://code.dennyzhang.com/tag/rectangle)

---

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.  

For example, given the following matrix:  

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

Return 6.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/maximal-rectangle)  

Credits To: [leetcode.com](https://leetcode.com/problems/maximal-rectangle/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/maximal-rectangle
    ## Basic Ideas: monotone stack
    ##       Based on another problem: https://code.dennyzhang.com/largest-rectangle-in-histogram
    ##
    ##       For each row, get the height
    ##       Find the max region of each row. Then get the global max
    ##
    ## Complexity: Time O(n*m), Space O(m)
    class Solution(object):
        def maximalRectangle(self, matrix):
            """
            :type matrix: List[List[str]]
            :rtype: int
            """
            row_count = len(matrix)
            if row_count == 0: return 0
            col_count = len(matrix[0])
            max_region = 0
            for i in range(0, row_count):
                for j in xrange(col_count):
                    matrix[i][j] = int(matrix[i][j])
                    # no need to add for first row
                    if i != 0:
                        if matrix[i][j] == 1:
                            matrix[i][j] += matrix[i-1][j]
                max_region = max(max_region, self.largestRectangleArea(matrix[i]))
            return max_region
    
        def largestRectangleArea(self, heights):
            """
            :type heights: List[int]
            :rtype: int
            """
            length = len(heights)
            next_smallers = [-1] * length
            stack = []
            max_width = 0
            # pad with fake items for the end
            for i in xrange(length+1):
                current = heights[i] if i != length else -1
                # When heights[i] is not greater than the stack top, it's the target of stack top
                while len(stack) != 0 and  current <= heights[stack[-1]]:
                    k = stack.pop()
                    h = heights[k]
                    left = -1 if len(stack) == 0 else stack[-1]
                    left = left + 1
                    right = i
                    max_width = max(max_width, h*(right-left))
                stack.append(i)
            return max_width