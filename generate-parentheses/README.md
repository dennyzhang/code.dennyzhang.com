# Leetcode: Generate Parentheses     :BLOG:Basic:


---

Generate Parentheses  

---

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.  

    For example, given n = 3, a solution set is:
    
    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/generate-parentheses)  

Credits To: [leetcode.com](https://leetcode.com/problems/generate-parentheses/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/generate-parentheses
    ## Basic Ideas: Use counter to make sure it's well-formed paretheses
    ##       Use BFS to generate the result
    ##       1. For each character, we can only print (, or )
    ##       2. unbalanced_count: How many unbalanced ( so far, 
    ##             printed_count: how many ( has already been alreay printed
    ##       3. When we can print (, if printed_count < n
    ##       4. When we can print ), if unbalanced_count > 0
    ## Complexity
    ## Sample Data:
    ##       ( stack: (
    ##       )
    class Solution(object):
        def generateParenthesis(self, n):
            """
            :type n: int
            :rtype: List[str]
            """
            if n<=0:
                return []
            res = []
            bfs_queue = []
            bfs_queue.append(("(", 1, 1))
            # loop for layer
            for i in xrange(n*2-1):
                for j in xrange(len(bfs_queue)):
                    # ('((()', 3, 2)
                    (output_str, printed_count, unbalanced_count) = bfs_queue[0]
                    del bfs_queue[0]
                    if printed_count < n:
                        bfs_queue.append(("%s(" % (output_str), \
                                            printed_count+1, unbalanced_count+1))
                    if unbalanced_count > 0:
                        bfs_queue.append(("%s)" % (output_str), \
                                            printed_count, unbalanced_count-1))
            for i in xrange(len(bfs_queue)):
                res.append(bfs_queue[i][0])
            return res