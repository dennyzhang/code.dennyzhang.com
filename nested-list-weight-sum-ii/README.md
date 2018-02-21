# Leetcode: Nested List Weight Sum II     :BLOG:Medium:


---

Nested List Weight Sum II  

---

Similar Problems:  

-   [Nested List Weight Sum](https://brain.dennyzhang.com/nested-list-weight-sum)
-   Tag: [#nestedlist](https://brain.dennyzhang.com/tag/nestedlist)

---

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.  

Each element is either an integer, or a list -- whose elements may also be integers or other lists.  

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.  

Example 1:  

    Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

Example 2:  

    Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/nested-list-weight-sum-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/nested-list-weight-sum-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/nested-list-weight-sum-ii
    ## Basic Ideas: BFS
    ##     Find the depest level. Then use BFS
    ##
    ## Complexity: Time O(n), Space O(n)
    # """
    # This is the interface that allows for creating nested lists.
    # You should not implement it, or speculate about its implementation
    # """
    #class NestedInteger(object):
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
    
    class Solution(object):
        def depthSumInverse(self, nestedList):
            """
            :type nestedList: List[NestedInteger]
            :rtype: int
            """
            import collections
            if len(nestedList) == 0: return 0
            deepest_level = self.findDepth(nestedList, 0)
            return self.myDepthSumInverse(nestedList, deepest_level)
    
        def myDepthSumInverse(self, nestedList, level):
            res = 0
            for item in nestedList:
                if item.isInteger(): res += item.getInteger()*level
                else:
                    res += self.myDepthSumInverse(item.getList(), level-1)
            return res
    
        def findDepth(self, nestedList, level):
            if len(nestedList) == 0: return 0
            deepest_level = level
            for item in nestedList:
                if item.isInteger(): 
                    deepest_level = max(deepest_level, level+1)
                    continue
                for p in item.getList():
                    if p.isInteger(): deepest_level = max(deepest_level, level+2)
                    else:
                        deepest_level = max(deepest_level, self.findDepth(p.getList(), level+2))
            return deepest_level