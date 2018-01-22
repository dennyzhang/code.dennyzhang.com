# Leetcode: Unique Binary Search Trees     :BLOG:Hard:


---

Unique Binary Search Trees  

---

Given n, how many structurally unique BST's (binary search trees) that store values 1&#x2026;n?  

    For example,
    Given n = 3, there are a total of 5 unique BST's.
    
       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/unique-binary-search-trees)  

Credits To: [leetcode.com](https://leetcode.com/problems/unique-binary-search-trees/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/unique-binary-search-trees
    class Solution(object):
        def numTrees(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n == 0: return 0
            if n == 1: return 1
            if n == 2: return 2
            if n > 2:
                return self.numTrees(n-1)*2+1