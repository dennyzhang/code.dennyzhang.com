# Leetcode: Largest Rectangle in Histogram     :BLOG:Hard:


---

Largest Rectangle in Histogram  

---

Similar Problems:  
-   [Leetcode: Maximal Rectangle](https://code.dennyzhang.com/maximal-rectangle)
-   [Review: Monotone Stack Or Monotone Queue Problems](https://code.dennyzhang.com/review-monotone), Tag: [monotone](https://code.dennyzhang.com/tag/monotone)
-   [Review: Rectangle Problems](https://code.dennyzhang.com/review-rectangle), Tag: [#rectangle](https://code.dennyzhang.com/tag/rectangle)

---

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.  

![img](//raw.githubusercontent.com/DennyZhang/challenges-leetcode-interesting/master/images/histogram.png)  
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].  

![img](//raw.githubusercontent.com/DennyZhang/challenges-leetcode-interesting/master/images/histogram_area.png)  

The largest rectangle is shown in the shaded area, which has area = 10 unit.  

For example,  
Given heights = [2,1,5,6,2,3],  
return 10.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/largest-rectangle-in-histogram)  

Credits To: [leetcode.com](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/largest-rectangle-in-histogram
    ## Basic Ideas: Monotone stack
    ##              For each element, find the next non-greater value
    ##     Key Questions: How to get the left?
    ##                    What if right is not found, any special logic?
    ##
    ## Complexity:
    class Solution(object):
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
    
    # s = Solution()
    # print s.largestRectangleArea([2, 1, 2]) # 3