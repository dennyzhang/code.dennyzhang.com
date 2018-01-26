# Leetcode: Verify Preorder Serialization of a Binary Tree     :BLOG:Basic:


---

Verify Preorder Serialization of a Binary Tree  

---

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.  

         _9_
        /   \
       3     2
      / \   / \
     4   1  #  6
    / \ / \   / \
    # # # #   # #

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.  

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.  

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.  

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".  

    Example 1:
    "9,3,4,#,#,1,#,#,2,#,6,#,#"
    Return true

    Example 2:
    "1,#"
    Return false

    Example 3:
    "9,#,#,1"
    Return false

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/verify-preorder-serialization-of-a-binary-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/verify-preorder-serialization-of-a-binary-tree
    ## Basic Ideas: Stack
    ##      If number, push.
    ##      If #, check stack head. 
    ##         If empty, return false; 
    ##         If #, the next element should be a node value. If not, return False
    ##         Pop them both. Keep checking, then push #
    ##      At the end, stack should have only one element. And it's #
    ##
    ##  Sample data: "#"
    ## Complexity: Time O(n), Space O(n)
    class Solution(object):
        def isValidSerialization(self, preorder):
            """
            :type preorder: str
            :rtype: bool
            """
            stack = []
            for element in preorder.split(','):
                if element != '#':
                    stack.append(element)
                else:
                    while True:
                        if len(stack) <= 1:
                            stack.append('#')
                            break
                        if stack[-1] != '#':
                            stack.append('#')
                            break
                        if stack[-1] == '#' and stack[-2] == '#': return False
                        # pop #, then pop value. Then plan to insert another '#'
                        stack.pop()
                        stack.pop()
                    else:
                        stack.append(element)
            return stack == ['#']