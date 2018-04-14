# Leetcode: Range Sum Query - Mutable     :BLOG:Amusing:


---

Range Sum Query - Mutable  

---

Similar Problems:  
-   [Range Addition](https://code.dennyzhang.com/range-addition)
-   [Review: Segment Tree Problems](https://code.dennyzhang.com/review-segmenttree)
-   [Review: Concurrency Problems](https://code.dennyzhang.com/review-concurrency)
-   [Review: Object-Oriented Design Problems](https://code.dennyzhang.com/review-oodesign)
-   Tag: [oodesign](https://code.dennyzhang.com/tag/oodesign), [#segmenttree](https://code.dennyzhang.com/tag/segmenttree), [#concurrency](https://code.dennyzhang.com/tag/concurrency)

---

Related Reading: [Segment Tree by geeksforgeeks.org](https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)  

Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.  

The update(i, val) function modifies nums by updating the element at index i to val.  

    Example:
    Given nums = [1, 3, 5]
    
    sumRange(0, 2) -> 9
    update(1, 2)
    sumRange(0, 2) -> 8

Note:  
-   The array is only modifiable by the update function.
-   You may assume the number of calls to update and sumRange function is distributed evenly.

    What if, update and sumRange function is not distributed evenly? 
    
    Let's say, the ratio of update_count/sumRange_count is 10000 or 0.0001?

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/range-sum-query-mutable)  

Credits To: [leetcode.com](https://leetcode.com/problems/range-sum-query-mutable/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/range-sum-query-mutable
    class NumArray(object):
    
        def __init__(self, nums):
            """
            :type nums: List[int]
            """
    
    
        def update(self, i, val):
            """
            :type i: int
            :type val: int
            :rtype: void
            """
    
    
        def sumRange(self, i, j):
            """
            :type i: int
            :type j: int
            :rtype: int
            """
    
    
    
    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # obj.update(i,val)
    # param_2 = obj.sumRange(i,j)