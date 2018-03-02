# Leetcode: Range Sum Query - Mutable     :BLOG:Amusing:


---

Range Sum Query - Mutable  

---

Similar Problems:  
-   [Range Addition](https://brain.dennyzhang.com/range-addition)
-   [Review: Segment Tree Problems](https://brain.dennyzhang.com/review-segmenttree), Tag: [#segmenttree](https://brain.dennyzhang.com/tag/segmenttree)
-   [Review: Concurrency Problems](https://brain.dennyzhang.com/review-concurrency), Tag: [#concurrency](https://brain.dennyzhang.com/tag/concurrency)
-   [Review: Object-Oriented Design Problems](https://brain.dennyzhang.com/review-oodesign), Tag: [oodesign](https://brain.dennyzhang.com/tag/oodesign)

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

    ## Blog link: https://brain.dennyzhang.com/range-sum-query-mutable
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