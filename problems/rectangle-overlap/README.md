
# Leetcode: Rectangle Overlap     :BLOG:Basic:

---

Rectangle Overlap  

---

Similar Problems:  

-   [Rectangle Area](https://code.dennyzhang.com/rectangle-area)
-   [Review: Rectangle Problems](https://code.dennyzhang.com/review-rectangle)
-   Tag: [#rectangle](https://code.dennyzhang.com/tag/rectangle)

---

A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.  

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.  

Given two rectangles, return whether they overlap.  

Example 1:  

    Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
    Output: true

Example 2:  

    Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
    Output: false

Notes:  

-   Both rectangles rec1 and rec2 are lists of 4 integers.
-   All coordinates in rectangles will be between -10^9 and 10^9.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/rectangle-overlap)  

Credits To: [leetcode.com](https://leetcode.com/problems/rectangle-overlap/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/rectangle-overlap
    ## Basic Ideas: Get overlapped region
    ## Complexity: Time O(1), Space O(1)
    class Solution:
        def isRectangleOverlap(self, rec1, rec2):
    	"""
    	:type rec1: List[int]
    	:type rec2: List[int]
    	:rtype: bool
    	"""
    	width = min(rec1[2], rec2[2])-max(rec1[0], rec2[0])
    	if width <= 0: return False
    	height = min(rec1[3], rec2[3])-max(rec1[1], rec2[1])
    	if height <= 0: return False
    	return True

