#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/sum-of-left-leaves/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-12 10:05:11>
##-------------------------------------------------------------------
#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Description :
##     https://leetcode.com/problems/sum-of-left-leaves/description/
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-20 16:55:53>
##-------------------------------------------------------------------
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
