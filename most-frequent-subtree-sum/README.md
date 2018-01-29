# Leetcode: Most Frequent Subtree Sum     :BLOG:Medium:


---

Most Frequent Subtree Sum  

---

Similar Problems:  
-   Tag: [binarytree](https://brain.dennyzhang.com/tag/binarytree)

---

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.  

Examples 1  

    Input:
    
      5
     /  \
    2   -3
    return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2  

    Input:
    
      5
     /  \
    2   -5
    return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/most-frequent-subtree-sum)  

Credits To: [leetcode.com](https://leetcode.com/problems/most-frequent-subtree-sum/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/most-frequent-subtree-sum
    ## Basic Ideas: post-order
    ##              For the result, build a map
    ##              Find the number of mast frequent occurency
    ##              Get the list matching the occurency
    ##
    ## Complexity: Time O(n), Space O(n)
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    import collections
    class Solution(object):
        def findFrequentTreeSum(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
    
            m = collections.defaultdict(lambda: 0)
            self.getSum(root, m)
    
            # find the most frequent count
            most_freq = 0
            for num in m:
                most_freq = max(most_freq, m[num])
    
            res = []
            # get the matched values
            for num in m:
                if m[num] == most_freq:
                    res.append(num)
            return res
    
        def getSum(self, root, m):
            """
            :type root: TreeNode
            :rtype: int
            """
            if root is None: return 0
            res = root.val + self.getSum(root.left, m) + self.getSum(root.right, m)
            m[res] += 1
            return res