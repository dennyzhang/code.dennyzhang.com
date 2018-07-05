# Leetcode: Sum of Left Leaves     :BLOG:Basic:


---

Sum of Left Leaves  

---

Find the sum of all left leaves in a given binary tree.  

    Example:
    
        3
       / \
      9  20
        /  \
       15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/sum-of-left-leaves)  

Credits To: [leetcode.com](https://leetcode.com/problems/sum-of-left-leaves/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/sum-of-left-leaves
    class Solution(object):
        ## Idea: BFS. (element, is_left)
        ##       DFS
        ## Complexity: 
        def sumOfLeftLeaves(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 0
    
            return self._sumOfLeftLeaves(root, False)
    
        def _sumOfLeftLeaves(self, root, is_left):
            if root is None:
                return 0
    
            if root.left is None and root.right is None:
                if is_left:
                    return root.val
                else:
                    return 0
    
            sum_value = 0
            if root.left:
                sum_value += self._sumOfLeftLeaves(root.left, True)
    
            if root.right:
                sum_value += self._sumOfLeftLeaves(root.right, False)
    
            return sum_value