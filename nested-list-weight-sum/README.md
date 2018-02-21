# Leetcode: Nested List Weight Sum     :BLOG:Basic:


---

Nested List Weight Sum  

---

Similar Problems:  
-   [Nested List Weight Sum II](https://brain.dennyzhang.com/nested-list-weight-sum-ii)
-   Tag: [#nestedlist](https://brain.dennyzhang.com/tag/nestedlist)

---

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.  

Each element is either an integer, or a list &#x2013; whose elements may also be integers or other lists.  

Example 1:  

    Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:  

    Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/nested-list-weight-sum)  

Credits To: [leetcode.com](https://leetcode.com/problems/nested-list-weight-sum/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/nested-list-weight-sum
    # """
    # This is the interface that allows for creating nested lists.
    # You should not implement it, or speculate about its implementation
    # """
    #class NestedInteger:
    #    def __init__(self, value=None):
    #        """
    #        If value is not specified, initializes an empty list.
    #        Otherwise initializes a single integer equal to value.
    #        """
    #
    #    def isInteger(self):
    #        """
    #        @return True if this NestedInteger holds a single integer, rather than a nested list.
    #        :rtype bool
    #        """
    #
    #    def add(self, elem):
    #        """
    #        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
    #        :rtype void
    #        """
    #
    #    def setInteger(self, value):
    #        """
    #        Set this NestedInteger to hold a single integer equal to value.
    #        :rtype void
    #        """
    #
    #    def getInteger(self):
    #        """
    #        @return the single integer that this NestedInteger holds, if it holds a single integer
    #        Return None if this NestedInteger holds a nested list
    #        :rtype int
    #        """
    #
    #    def getList(self):
    #        """
    #        @return the nested list that this NestedInteger holds, if it holds a nested list
    #        Return None if this NestedInteger holds a single integer
    #        :rtype List[NestedInteger]
    #        """
    
    class Solution:
        ## Basic Ideas: dfs
        ##
        ## Complexity: Time O(n), Space O(k). Depth of the deepest element
        def depthSum(self, nestedList):
            """
            :type nestedList: List[NestedInteger]
            :rtype: int
            """
            return self.myDepthSum(nestedList, 1)
    
        def myDepthSum(self, nestedList, level):
            """
            :type nestedList: List[NestedInteger]
            :rtype: int
            """
            res = 0
            for item in nestedList:
                if item.isInteger():
                    res += item.getInteger()*level
                else:
                    res += self.myDepthSum(item.getList(), level+1)
            return res