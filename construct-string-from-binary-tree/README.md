# Leetcode: Construct String from Binary Tree     :BLOG:Basic:


---

Construct String from Binary Tree  

---

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.  

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.  

    Example 1:
    Input: Binary tree: [1,2,3,4]
           1
         /   \
        2     3
       /    
      4     
    
    Output: "1(2(4))(3)"
    
    Explanation: Originallay it needs to be "1(2(4)())(3()())", 
    but you need to omit all the unnecessary empty parenthesis pairs. 
    And it will be "1(2(4))(3)".

    Example 2:
    Input: Binary tree: [1,2,3,null,4]
           1
         /   \
        2     3
         \  
          4 
    
    Output: "1(2()(4))(3)"
    
    Explanation: Almost the same as the first example, 
    except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/construct-string-from-binary-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/construct-string-from-binary-tree/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/construct-string-from-binary-tree
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def tree2str(self, t):
            """
            :type t: TreeNode
            :rtype: str
            """
            ## Idea: recursive
            ## Complexity
            if t is None:
                return ""
            if t.left is None and t.right is None:
                return str(t.val)
    
            res = str(t.val)
            if t.left:
                res = "%s(%s)" % (res, self.tree2str(t.left))
            else:
                res = "%s()" % (res)
    
            if t.right:
                res = "%s(%s)" % (res, self.tree2str(t.right))
    
            return res